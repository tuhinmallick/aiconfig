from aiconfig.model_parser import ModelParser


class MockModelParser(ModelParser):
    def __init__(self):
        pass

    def id(self):
        return "mock_model_parser"

    def serialize(self):
        return

    def deserialize(self):
        return

    def run(self):
        return

    def get_output_text():
        return
