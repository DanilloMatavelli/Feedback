from hashlib import sha256

senha = "teste"
senha_criptografada = sha256(senha.encode()).hexdigest()

print(senha_criptografada)