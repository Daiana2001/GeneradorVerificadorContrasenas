#!/usr/bin/env python3
"""
generador_contrasenas.py
Generador de contraseñas seguras usando secrets (aleatoriedad criptográfica).
o tambien verifica la seguridad de una contraseña dada.


"""

import random
import string
import math

def calcular_entropia(password, charset_size):
    """Calcula la entropía de una contraseña en bits."""
    return len(password) * math.log2(charset_size)

def verificar_contrasena(password):
    """Verifica si una contraseña es segura o no."""
    tiene_minuscula = any(c.islower() for c in password)
    tiene_mayuscula = any(c.isupper() for c in password)
    tiene_digito = any(c.isdigit() for c in password)
    tiene_simbolo = any(c in string.punctuation for c in password)

    categorias = sum([tiene_minuscula, tiene_mayuscula, tiene_digito, tiene_simbolo])

    # Calcular entropía
    charset_size = 0
    if tiene_minuscula: charset_size += 26
    if tiene_mayuscula: charset_size += 26
    if tiene_digito: charset_size += 10
    if tiene_simbolo: charset_size += len(string.punctuation)

    entropia = calcular_entropia(password, charset_size) if charset_size > 0 else 0

    # Evaluación de seguridad
    if len(password) < 8 or categorias < 3 or entropia < 50:
        nivel = "Débil ❌"
    elif len(password) >= 12 and categorias == 4 and entropia >= 70:
        nivel = "Fuerte ✅"
    else:
        nivel = "Media ⚠️"

    print("\n🔎 Análisis de tu contraseña:")
    print(f"- Longitud: {len(password)}")
    print(f"- Mayúsculas: {'Sí' if tiene_mayuscula else 'No'}")
    print(f"- Minúsculas: {'Sí' if tiene_minuscula else 'No'}")
    print(f"- Dígitos: {'Sí' if tiene_digito else 'No'}")
    print(f"- Símbolos: {'Sí' if tiene_simbolo else 'No'}")
    print(f"- Entropía estimada: {entropia:.2f} bits")
    print(f"=> Nivel de seguridad: {nivel}\n")

def generar_contrasena(longitud=12, excluir_similares=True):
    """Genera una contraseña segura."""
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    digitos = string.digits
    simbolos = string.punctuation

    if excluir_similares:
        similares = "ilLI|1oO0"
        minusculas = ''.join(c for c in minusculas if c not in similares)
        mayusculas = ''.join(c for c in mayusculas if c not in similares)
        digitos = ''.join(c for c in digitos if c not in similares)

    todos = minusculas + mayusculas + digitos + simbolos

    print("\n📋 La contraseña generada tendrá:")
    print(f"- Longitud: {longitud}")
    print("- Incluirá: mayúsculas, minúsculas, dígitos y símbolos")
    print(f"- Caracteres posibles: {todos}\n")

    # Garantizamos al menos un caracter de cada tipo
    password = [
        random.choice(minusculas),
        random.choice(mayusculas),
        random.choice(digitos),
        random.choice(simbolos)
    ]

    # Completar hasta la longitud deseada
    password += [random.choice(todos) for _ in range(longitud - 4)]
    random.shuffle(password)

    resultado = ''.join(password)
    print(f"🔐 Contraseña generada: {resultado}\n")
    verificar_contrasena(resultado)

def menu():
    print("=== Gestor de Contraseñas ===")
    print("1. Generar una contraseña segura")
    print("2. Verificar tu propia contraseña")
    opcion = input("Elegí una opción (1/2): ")

    if opcion == "1":
        longitud = input("📏 Ingresá la longitud (Enter = 12 por defecto): ")
        longitud = int(longitud) if longitud.strip() != "" else 12
        generar_contrasena(longitud)
    elif opcion == "2":
        password = input("✍️ Escribí tu contraseña para analizar: ")
        verificar_contrasena(password)
    else:
        print("❌ Opción no válida.")

if __name__ == "__main__":
    menu()
