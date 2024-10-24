
<p align="center">
    <img src="pii_cover.jpeg" alt="PII Masker Cover" style="width: 100%; max-width: 900px;">
</p>

<p align="center">
PII Masker is an advanced open-source tool that protects your sensitive data using state-of-the-art AI, powered by DeBERTa-v3
</p>

<p align="center">
<a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
<a href="https://python.org"><img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="Python: 3.8+"></a>
<a href="https://milvus.io/"><img src="https://img.shields.io/badge/Milvus-vector--database-blue.svg" alt="Milvus"></a>
<a href="https://huggingface.co/"><img src="https://img.shields.io/badge/HuggingFace-models-yellow.svg" alt="Hugging Face"></a>
</p>

<p align="center">
    <a href="#-key-features"><b>Features</b></a> •
    <a href="#-installation"><b>Installation</b></a> •
    <a href="#-quick-start"><b>Quick Start</b></a> •
    <a href="#-how-it-works"><b>How It Works</b></a> •
    <a href="#-Contributing"><b>Contributing</b></a>
</p>


PII Masker is an advanced open-source tool designed to protect your sensitive data by leveraging cutting-edge AI models. Built on top of DeBERTa-v3, this tool ensures high-precision detection and masking of Personally Identifiable Information (PII), making it a perfect fit for any data-sensitive workflows. Whether you're handling customer data, performing data analysis, or ensuring compliance with privacy regulations, PII Masker provides a robust, scalable solution to keep your information secure.


## Why Choose PII Masker?

When handling sensitive information, it's crucial to use tools that not only perform well but also ensure compliance and protect privacy. Here's why PII Masker stands out:

- **High Precision**: Utilizes DeBERTa-v3 for accurate detection and masking of various PII types.
- **Compliance Friendly**: Designed to help organizations meet privacy laws and regulations.
- **Flexible Integration**: Offers easy integration with existing systems through a simple Python API.


## ✨ Key Features

* 🔒 **Comprehensive Protection**: Identifies and masks multiple PII types including names, addresses, phone numbers, and more
* 🚀 **High Performance**: Powered by DeBERTa-v3 with 1024 token support for processing longer documents
* 🎯 **Precision Focused**: Advanced NLP model fine-tuned specifically for PII detection
* 📊 **Structured Output**: Get both masked text and structured PII dictionary
* 🔄 **Easy Integration**: Simple Python API for seamless integration into your workflow

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pii-masker.git
cd pii-masker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the model:
```bash
# Option 1: Manual download
# Visit: https://huggingface.co/hydroxai/pii_model_weight
# Place files in: pii-masker/output_model/deberta3base_1024/
```

## 🚀 Quick Start

1. Change to the `pii-masker` directory:
   ```bash
   cd pii-masker

2. Use the following code to get started:
   ```python
   from model import PIIMasker
    
   # Initialize the PIIMasker
   masker = PIIMasker()
    
   # Mask PII in your text
   text = "John Doe lives at 1234 Elm St."
   masked_text, pii_dict = masker.mask_pii(text)
    
   print(masked_text)
   # Output: "[NAME] lives at [ADDRESS]"
   ```

## 🔍 How It Works

PII Masker employs a sophisticated pipeline powered by DeBERTa-v3:

1. **Tokenization** → Smart text splitting for optimal processing
2. **Model Inference** → AI-powered PII detection
3. **Entity Recognition** → Precise identification of sensitive data
4. **Masking** → Secure replacement of PII with placeholders
5. **Data Extraction** → Structured output for further processing

## 🛠️ Advanced Usage

Check out our detailed examples:
- [RAG Integration Example](RAG_with_pii_and_milvus.ipynb)
  
## 🤝 Contributing

Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



## 🙏 Acknowledgments

Special thanks to:
- [Microsoft](https://github.com/microsoft/DeBERTa) for the DeBERTa model
- [Hugging Face](https://huggingface.co) for model hosting and transformers library
- [Zilliz](https://zilliz.com) for their support and Milvus, the vector database powering our solution
- All our contributors and supporters


---

<p align="center">
Made with ❤️ for the privacy-conscious developer community
</p>
