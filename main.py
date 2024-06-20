import argparse
import logging
import os
import time
from pathlib import Path

import img2pdf

if __name__ == "__main__":
    logging.getLogger("img2pdf").setLevel("ERROR")
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdf_name", action="store", help="Provide name of the pdf to be created")
    parser.add_argument("--path", action="store", help="Provide path for images to join into PDF file")
    pdf_name = parser.parse_args().pdf_name
    path = Path(parser.parse_args().path)
    print(f"Generating file './output_files/{pdf_name}.pdf' file from {len(os.listdir(path))} images...")
    Path("output_files").mkdir(exist_ok=True)
    start = time.time()
    with open(f"./output_files/{pdf_name}.pdf", "wb") as f:
        # https://stackoverflow.com/a/33159707
        f.write(img2pdf.convert([path.joinpath(file_name) for file_name in
                                 sorted(os.listdir(path), key=lambda image_name: int("".join(filter(str.isdigit, image_name))))]))
    print(f"File './output_files/{pdf_name}.pdf' successfully generated in {round(time.time() - start, 2)}s!")
