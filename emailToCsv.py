# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 17:03:48 2021

@author: sak36
"""

# File Prompt

import tkinter as tk
from tkinter import filedialog
import string

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()


#Parse Email
import os
from email import policy
from email.parser import BytesParser

directory = file_path
with open(directory+'\\directory.csv', 'w', encoding='UTF8', newline='') as f:
    f.write('')
    for filename in os.listdir(directory):
        if filename.endswith(".eml"):
            payload = '"'
            print(os.path.join(directory, filename))
            with open(directory+'\\'+filename, 'rb') as fp:
                msg = BytesParser(policy=policy.default).parse(fp)
            print('To:', msg['to'])
            print('From:', msg['from'])
            #payload+=(msg['from'])
            print('Subject:', msg['subject'])
            if msg['subject'] is None:
                continue
            if msg['subject']=='':
                continue
            payload+=(msg['subject'])
            val = msg.get_body('plain')
            '''TODO: Replace '\n' w/ ' ' and add body data
            if val is not None:
                print('Body:', val.as_bytes().decode(encoding='UTF-8'))
                payload+=(val.as_bytes().decode(encoding='UTF-8'))
                payload.translate(str.maketrans('', '', string.punctuation))
                #f.write(payload)
            '''
            print()
            payload+='", 0\n'
            print(payload)
            f.write(payload)
        else:
            continue

