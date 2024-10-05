# PII Masker

PII Masker is a Python tool designed to identify and mask Personally Identifiable Information (PII) in text using a pre-trained NLP model based on the DeBERTa-v3 architecture.

## Features

* Masks various types of PII, including names, addresses, phone numbers, email addresses, and more.
* Uses a pre-trained model based on DeBERTa-v3-base with a maximum sequence length of 1024 tokens.
* Provides both masked text output and a dictionary of identified PII.

## How It Works

PII Masker uses a fine-tuned DeBERTa-v3 model to perform Named Entity Recognition (NER) on input text, specifically targeting PII entities. Here's a brief overview of the process:

1. **Tokenization**: The input text is tokenized using the DeBERTa tokenizer, which splits the text into subword units.

2. **Model Inference**: The tokenized input is passed through the pre-trained DeBERTa model, which has been fine-tuned on PII detection tasks. The model outputs probability distributions for each token, indicating the likelihood of it belonging to various PII categories.

3. **Entity Recognition**: The output probabilities are processed to identify continuous spans of tokens that represent PII entities. This step uses a combination of the model's predictions and post-processing rules to accurately identify entity boundaries.

4. **Masking**: Once PII entities are identified, the original text is masked by replacing the identified spans with placeholders (e.g., [NAME], [ADDRESS], etc.) while maintaining the original text structure.

5. **PII Extraction**: In addition to masking, the tool extracts the identified PII into a structured dictionary, allowing for further processing or analysis if needed.

The use of DeBERTa-v3 as the base model provides several advantages:

- Improved context understanding through its enhanced masked language model pre-training.
- Better handling of long-range dependencies in text, which is crucial for accurate PII detection.
- Increased robustness to various text formats and styles.

## Installation

1. Clone this repository
2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Download the pre-trained model weights:
   * Go to the Hugging Face model repository: [hydroxai/pii_model_weight](https://huggingface.co/hydroxai/pii_model_weight)
   * Download the model weights
   * Place the downloaded files in the following directory:

```
pii-masker/output_model/deberta3base_1024/
```

## Usage

```python
from pii_masker import PIIMasker

masker = PIIMasker()
input_text = "John Doe's SSN is 123-45-6789 and he lives at 1234 Elm St."
masked_text, pii_dict = masker.mask_pii(input_text)

print(masked_text)
print(pii_dict)
```

This will output the masked text and a dictionary containing the identified PII entities.

For a complete usage example, refer to `build_RAG_with_pii_and_milvus.ipynb`.

## Customization

The PII Masker can be customized to detect and mask specific types of PII based on your requirements. This can be done by fine-tuning the model on a dataset that includes the desired PII categories or by adjusting the post-processing rules in the `mask_pii` method.
