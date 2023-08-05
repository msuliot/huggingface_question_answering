from transformers import pipeline

import os
from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN') # api key for huggingface.co in .env file
model_name = os.getenv('MODEL_NAME') # model name for huggingface.co in .env file
pipeline_task = os.getenv('PIPELINE_TASK') # pipeline task for huggingface.co in .env file
os.environ['TOKENIZERS_PARALLELISM'] = 'true'


def hf_pipeline(question, context):
    qc = {"question": question, "context": context}
    pipe = pipeline(task=pipeline_task, model=model_name)
    output = pipe(qc)
    return output


def main():
    question = "Why is model conversion important?"
    context = "The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks."
    return_value = hf_pipeline(question, context)
    print(return_value)


if __name__ == "__main__":
    main() 