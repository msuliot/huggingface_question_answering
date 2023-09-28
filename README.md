# Hugging Face - Question Answering
This is a simple example of how to use the Hugging Face Hub for question answering on provided content.

## YouTube Video Tutorial for this GitHub Repository
[Hugging Face - Question & Answering](https://youtu.be/gHEbNhX0sSQ)

## The basics

1. Must have Python3.
2. Get repository
```bash
git clone https://github.com/msuliot/huggingface_question_answering.git 
```
3. use pip3 to install any dependencies.
```bash
pip3 install -r requirements.txt
```

## Hugging Face Access Token

You'll need to sign up for an account on https://huggingface.co/ and get an access token.
Make sure to get an access token key from https://huggingface.co/settings/tokens

Create a ".env" file in the project root directory and add the following:
```bash
HUGGINGFACEHUB_API_TOKEN = 'hf_XXXXXXXX'
MODEL_NAME = 'deepset/roberta-base-squad2'
PIPELINE_TASK = "question-answering"
```

# Instructions:

There are three different examples of how to use the Hugging Face Hub.

## Run the API script
```bash
python3 api.py
```

## Run the pipeline script
```bash
python3 pipeline.py
```

## Run the local script
```bash
python3 local.py
```
This will download the model and tokenizer to your local machine and run on your local machine.
Supported tensors are 
- PyTorch 
- TensorFlow

## Hugging Face Hub API 
https://huggingface.co/deepset/roberta-base-squad2
- modelId: deepset/roberta-base-squad2
- pipeline_tag: question-answering
- library_name: transformers
- architectures: RobertaForQuestionAnswering
- transformersInfo: auto_model: AutoModelForQuestionAnswering
- transformersInfo: pipeline_tag: question-answering
- transformersInfo: processor: AutoTokenizer
- task_specific_params: None