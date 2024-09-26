import torch
import unittest
from transformers import AutoTokenizer, AutoModelForTokenClassification
import re
import os

class PIIMasker:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_dir, "output_model", "deberta3base_1024")
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForTokenClassification.from_pretrained(model_path)
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model.to(self.device)

    def mask_pii(self, input_text):
        inputs = self.tokenizer(input_text, return_tensors="pt", padding=True, truncation=True)

        with torch.no_grad():
            outputs = self.model(**{k: v.to(self.device) for k, v in inputs.items()})

        logits = outputs.logits
        predictions = torch.argmax(logits, dim=2)
        predicted_labels = [self.model.config.id2label[pred.item()] for pred in predictions[0]]

        result_dict = {}
        for word, label in zip(self.tokenizer.tokenize(input_text), predicted_labels):
            result_dict[word] = label.replace('_STUDENT', '')

        # Initialize the dictionary to hold SSNs
        ssn_dict = self.extract_ssn(input_text)

        output = []
        previous_value = None
        pii_dict = {}  # Initialize the dictionary here

        for key, value in result_dict.items():
            key = key.replace('▁', ' ')

            if value == 'O':
                output.append(key.strip())
            else:
                if previous_value != value:
                    output.append(f"[{value}]")
                if value not in pii_dict:
                    pii_dict[value] = []
                pii_dict[value].append(key.strip())

            previous_value = value

        masked_text = ' '.join(output)

        # Combine ssn_dict into pii_dict
        pii_dict.update(ssn_dict)

        return masked_text, pii_dict

    @staticmethod
    def extract_ssn(input_string):
        ssn_pattern = r'\b(\d{3}-\d{2}-\d{4}|\d{9})\b'
        ssn_dict = {}
        matches = re.findall(ssn_pattern, input_string)
        for ssn in matches:
            ssn_dict[ssn] = 'SSN'  # Directly use the matched SSN
        return ssn_dict

if __name__ == "__main__":
    class TestPIIMasker(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            # 在测试开始前加载模型
            cls.masker = PIIMasker()
            
        def test_mask_pii(self):
            input_text = "My name is John Doe and my SSN is 123-45-6789."
            masked_text, _ = self.masker.mask_pii(input_text)

            # 检查输出是否包含预期的掩码文本
            self.assertIn("[B-NAME]", masked_text)  # 假设掩码为 [NAME]

        def test_extract_ssn(self):
            input_string = "My SSN is 987654320."
            ssn_dict = self.masker.extract_ssn(input_string)

            # 检查提取的 SSN 是否正确
            self.assertIn("987654320", ssn_dict)  

    unittest.main()