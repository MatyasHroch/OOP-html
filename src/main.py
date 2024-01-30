# input, img

from tags.leaf_tags.img import Img
from tags.leaf_tags.input import Input

# , select, a, div a form
from tags.pair_tags.a import A
from tags.pair_tags.div import Div
from tags.pair_tags.form import Form
from tags.pair_tags.select import Select


print("Hello World")

form_tag = Form()
form_content = [Img(), Input(), Select(), A(), Div()]

for tag in form_content:
    form_tag + tag

print(form_tag)
