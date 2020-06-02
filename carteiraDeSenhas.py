#! /usr/bin/env python3
# carteitaDeSenhas.py - Armazena as senhas de contas num Dicionário e envia ao usuário por clippboard

import sys, pyperclip

dicionario_senhas = {'email' : 'teste1234', 'blog': 'segredo3321', 'comum' : '1234567'}


if len(sys.argv) < 2:
    sys.exit("Este programa necessita de um argumento. Ex. nomeDoprograma argumento")
else:
    conta = sys.argv[1]


if conta in dicionario_senhas:
    pyperclip.copy(dicionario_senhas[conta])
else:
   print("A conta {} não foi encontrada".format(conta))              