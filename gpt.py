import google.generativeai as palm
from dotenv import load_dotenv

load_dotenv()


model=[]
for i in palm.list_models():
    if "generateText" in i.supported_generation_methods:
        model.append(i)


models=model[0].name


def palm_output(input_text):
    completion=palm.generate_text(
    model=models,
    prompt=input_text,
    temperature=0.9,
    max_output_tokens=1000
    )

    final=completion.result
    return final