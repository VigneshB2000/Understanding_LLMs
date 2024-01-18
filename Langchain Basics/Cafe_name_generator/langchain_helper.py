from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
import os
import configparser

config = configparser.RawConfigParser()
config.read('../../config.config')
openapi_key = config.get('Keys', 'openapi_key')
os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.7)

def generate_cafe_name_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template='Suggest me a fancy name for {cuisine} cafe'
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='cafe_name')

    prompt_template_items = PromptTemplate(
        input_variables=['cafe_name'],
        template='Suggest some menu items for {cafe_name} cafe and return as comma seperated list.'
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='menu_items')

    chain = SequentialChain(
        chains=[name_chain, food_items_chain],
        input_variables=['cuisine'],
        output_variables=['cafe_name', 'menu_items']
    )

    response = chain({'cuisine': cuisine})
    return response


if __name__ == '__main__':
    print(generate_cafe_name_items('Italian'))
