# rm4sccdec for Python 3
## Decoder for the RM4SCC (Royal Mail 4-State Customer Code)

Based on the original work from [cfax in Python 2.7](https://github.com/cfax/rm4sccdec). 

This version is a fork brought up to date and running on Python 3. 

No pyenv included, but requirements are in `requirements.txt` 

## Install

- Use Pip to install dependencies: `pip install -r requirements.txt`
- Run the code: `python3 main.py image.png` 

You need to specify the image you'd like to decode. In response, you will get the raw string data (including the checksum). 
