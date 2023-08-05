from transformers import pipeline, AutoTokenizer
from transformers import RobertaForQuestionAnswering, TFRobertaForQuestionAnswering

import os
from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv('HUGGINGFACEHUB_API_TOKEN') # api key for huggingface.co in .env file
model_name = os.getenv('MODEL_NAME') # model name for huggingface.co in .env file
pipeline_task = os.getenv('PIPELINE_TASK') # pipeline task for huggingface.co in .env file
os.environ['TOKENIZERS_PARALLELISM'] = 'true'


def hf_local(question, context):
    qc = {"question": question, "context": context}
    # This will download the model and tokenizer to your local machine and run on your local machine. 
    # saved and cached ~/.cache/huggingface
    tokenizer = AutoTokenizer.from_pretrained(model_name, return_tensors="pt") # return_tensors="pt" or "tf"
    model = RobertaForQuestionAnswering.from_pretrained(model_name) 
    pipe = pipeline(pipeline_task, model=model, tokenizer=tokenizer)
    output = pipe(qc)
    return output


def main():
    question = "Why is model conversion important?"
    context = "The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks."
    return_value = hf_local(question, context)
    print(return_value)

if __name__ == "__main__":
    main() 