from typing import cast
from PIL import Image
from PIL.PyAccess import PyAccess


def one_bitify_image(
        input_file_name: str,
        output_file_name: str) -> None:
    BLACK: int = 0
    WHITE: int = 1
    THRESHOLD: int = 128
    with Image.open(input_file_name) as input_file:
        input_file: Image.Image
        pixin: PyAccess = cast(PyAccess, input_file.load())
        width: int
        height: int
        width, height = input_file.size
    output_file: Image.Image = Image.new('1', (width, height))
    pixout: PyAccess = cast(PyAccess, output_file.load())
    row: int
    col: int
    for row in range(height):
        for col in range(width):
            red: int
            green: int
            blue: int
            red, green, blue = pixin[col, row]  # type: ignore
            average: int = (red + green + blue) // 3
            pixout[col, row] = BLACK if average < THRESHOLD else WHITE
    output_file.save(output_file_name)

if __name__ == '__main__':
    one_bitify_image('scarlett.png', 'scarlett_one_bit.png')
