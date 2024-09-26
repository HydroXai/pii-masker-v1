# PII Masker

PII Masker is a Python tool designed to identify and mask Personally Identifiable Information (PII) in text using a pre-trained NLP model.

## Features

- Masks various types of PII, including names, addresses, phone numbers, email addresses, and more.
- Uses a pre-trained model based on DeBERTa-v3-base with a maximum sequence length of 1024 tokens.
- Provides both masked text output and a dictionary of identified PII.

## Installation

1. Clone this repository

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Download the pre-trained model weights:
   - Go to the Hugging Face model repository: [xuyingliKepler/model_weight](https://huggingface.co/xuyingliKepler/model_weight)
   - Download the model weights
   - Place the downloaded files in the following directory:
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
