import ddddocr

class CaptchaSolver:
    def __init__(self):
        self.ocr = ddddocr.DdddOcr()

    def solve(self, image_bytes):
        return self.ocr.classification(image_bytes)
