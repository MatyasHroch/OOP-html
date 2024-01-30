class TextTag:
    def __init__(self, text=""):
        self.text = text

    def render(self, context):
        return self.text
