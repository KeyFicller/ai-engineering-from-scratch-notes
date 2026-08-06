
class SectionPrinter():
    def __init__(self, section_name):
        self.section_name = section_name

    def __enter__(self):
        print(self.section_name.center(60, "="))

    def __exit__(self, exc_type, exc_value, traceback):
        print("=" * 60)