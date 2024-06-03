from langchain_community.llms import Ollama

import MAPPING
from PROMPTS import IMAGE_PROMPT, SPARQL_INSERT_PROMPT, SPARQL_MAPPING_INPUT, SPARQL_CORRECTION_PROMPT, JSON_GENERATION_PROMPT, JSON_MAPPING_PROMPT

llama3 = Ollama(model="llama3")
# llama3.invoke("Who are you?")
#
# for chunks in llama3.stream("Who are you?"):
#     print(chunks)

bakllava = Ollama(model="llava")

from IPython.display import HTML, display
from PIL import Image
from io import BytesIO
import base64

def convert_to_bas64(pil_image):
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str


def plt_img_base64(img_base64):
    image_html = f'<img src="data:image/jpeg;base64,{img_base64}">'
    display(HTML(image_html))

file_path = "../pedestrian_perspective/download.jpg"
pil_image = Image.open(file_path)
img_base64 = convert_to_bas64(pil_image)
plt_img_base64(img_base64)

llm_with_image_context = bakllava.bind(images=[img_base64])
img_result = llm_with_image_context.invoke(IMAGE_PROMPT.format(question="How many people are there in the image?"))
print(img_result)
rdf_result = llama3.invoke(JSON_GENERATION_PROMPT + JSON_MAPPING_PROMPT.format(mapping=MAPPING.PEOPLE_COUNT, text=img_result))
print(rdf_result)
# corrected_result = llama3.invoke(SPARQL_CORRECTION_PROMPT.format(query=rdf_result))
# print(corrected_result)



