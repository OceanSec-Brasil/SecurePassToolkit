import random
import re
import string
import argparse

def generate_password(length=12, use_special_chars=True, forbidden_words=None):
    chars = string.ascii_letters + string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''
    while True:
        password = ''.join(random.choice(chars) for _ in range(length))
        if forbidden_words:
            if all(word.lower() not in password.lower() for word in forbidden_words):
                break
        else:
            break
    return password

def evaluate_password(password):
    score = 0
    if re.search("[a-z]", password): 
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    return score

def bulk_evaluate(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    for line in lines:
        password = line.strip()
        print(f"Evaluating: {password} - Score: {evaluate_password(password)}")

def security_recommendation(score):
    recommendations = {
        1: "Adicione maiúsculas, números e símbolos para torná-la mais segura.",
        2: "Adicione números e símbolos para aumentar a segurança.",
        3: "Adicione símbolos para fortalecer a senha.",
        4: "A senha é forte."
    }
    return recommendations.get(score, "Senha muito fraca. Recrie.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gerador e Avaliador de Senhas Fortes')
    parser.add_argument('--generate', type=int, help='Gerar uma senha forte com o comprimento especificado')
    parser.add_argument('--evaluate', type=str, help='Avaliar uma senha fornecida')
    parser.add_argument('--bulk_evaluate', type=str, help='Avaliar múltiplas senhas de um arquivo')
    parser.add_argument('--forbidden_words', type=str, nargs='+', help='Lista de palavras proibidas na senha gerada')
    args = parser.parse_args()

    if args.generate:
        password = generate_password(args.generate, forbidden_words=args.forbidden_words)
        print(f"Senha Gerada: {password}")

    if args.evaluate:
        score = evaluate_password(args.evaluate)
        print(f"Avaliação de Senha: {score}")
        print(f"Sugestão de Segurança: {security_recommendation(score)}")

    if args.bulk_evaluate:
        bulk_evaluate(args.bulk_evaluate)
