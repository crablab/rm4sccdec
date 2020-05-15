# rm4sccdec for Python 3
## Decoder for the RM4SCC (Royal Mail 4-State Customer Code)

Based on the original work from [cfax in Python 2.7](https://github.com/cfax/rm4sccdec). 

This version is a fork brought up to date and running on Python 3. 

No pyenv included, but requirements are in `requirements.txt` 

## What is it? 

Royal Mail use what is known as the State Customer Code (or Customer Bar Code) to identify mail in automatic sorting machines. 

The also use a variant of this known as Mailmark-C and Mailmark-L to encode sorting and OCR address data on mail, during sortation and delivery. 

More information from [Wikipedia](https://en.wikipedia.org/wiki/RM4SCC)

## Install

- Use Pip to install dependencies: `pip install -r requirements.txt`
- Import the library: `from rm4sccdec import converter`
- Instantiate the class: `cbc_conv = converter.converter()`
- Decode your image: `decoded_data = cbc_conv.decode("myimage.png")`

You need to specify the image you'd like to decode. In response, you will get the raw string data (including the checksum). 