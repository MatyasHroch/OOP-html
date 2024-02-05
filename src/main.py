# input, img
from tags.leaf_tags.img import Img
from tags.leaf_tags.input import Input


# select, a, div a form
from tags.pair_tags.a import A
from tags.pair_tags.div import Div
from tags.pair_tags.form import Form
from tags.pair_tags.select import Select

# text_tag
from tags.leaf_tags.text_tag import TextTag


print("Lets create a form with some tags inside:\n")

form_tag = Form()

div_tag = Div()
# div_tag.append_class("row")
div_tag.append_children([Input("text"), Select()])

a_tag = A("google.com")
a_tag + Img("./media/pictures/home.jpg")  # using the __add__ operator

text_tag = TextTag("This is a text for the form")

form_tag.append_children([text_tag, a_tag, div_tag])


print(form_tag)
