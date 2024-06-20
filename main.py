import argparse
import os
import time
from pathlib import Path

from PIL import Image


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf_name", action="store", help="Provide name of the pdf to be created")
    parser.add_argument("--path", action="store", help="Provide path for images to join into PDF file")
    pdf_name = parser.parse_args().pdf_name
    path = Path(parser.parse_args().path)
    # https://stackoverflow.com/a/33159707
    print(f"Storing {len(os.listdir(path))} images from '{path}'...")
    images = [Image.open(image_path) for image_path in [path.joinpath(file_name) for file_name in
                                                        sorted(os.listdir(path), key=lambda image_name: int("".join(filter(str.isdigit, image_name))))]]
    for image in images:
        image.convert("RGB")
    print(f"Generating file './output_files/{pdf_name}.pdf' file...")
    Path("output_files").mkdir(exist_ok=True)
    start = time.time()
    images[0].save(Path("output_files").joinpath(f"{pdf_name}.pdf"), save_all=True, append_images=images[1:])
    print(f"File './output_files/{pdf_name}.pdf' successfully generated in {round(time.time() - start, 2)}s!")
