class Document:
    def print_preview(self):
        pass

class WordDocument(Document):
    def print_preview(self):
        print("Word fayli: sahifa tartibi korsatilmoqda ")

class PdfDocument(Document):
    def print_preview(self):
        print("PDF fayli: statik sahifa korinmoqda ")

word = WordDocument()
word.print_preview()

pdf = PdfDocument()
pdf.print_preview()
