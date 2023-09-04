# Gerador e Avaliador de Senhas Fortes

#Descrição

Este projeto contém um script em Python para gerar senhas fortes e avaliar a força das senhas existentes. A ferramenta também permite a avaliação em lote de senhas a partir de um arquivo de texto. Além disso, o usuário pode especificar palavras que são proibidas de aparecer na senha gerada.

#Funcionalidades

- Geração de Senha: Cria uma senha segura com a combinação de caracteres minúsculos, maiúsculos, números e símbolos especiais.
- Avaliação de Senha: Fornece um escore de 1 a 4, indicando a força da senha.
- Avaliação em Lote: Avalia a força de múltiplas senhas a partir de um arquivo de texto.
- Palavras Proibidas: Permite ao usuário especificar palavras que não devem ser incluídas na senha.

#Como Usar

Requisitos:
- Python 3.x

#Instalação

Clone o repositório:
```
git clone https://github.com/OceanSec/PasswordTool.git
```
#Exemplos de Uso

Para gerar uma senha de 16 caracteres:
```
python script.py --generate 16
```
Para avaliar uma senha:
```
python script.py --evaluate "SuaSenha"
```
```
python script.py --bulk_evaluate "caminho/para/arquivo.txt"
```
Para gerar uma senha, excluindo palavras proibidas:
```
python script.py --generate 16 --forbidden_words abc 123
```
