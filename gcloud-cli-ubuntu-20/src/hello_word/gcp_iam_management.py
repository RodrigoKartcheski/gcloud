import subprocess
from config import comandos_iam, user_email, service_account

user_email=user_email
service_account=service_account
comandos=comandos_iam

# Executar cada comando
for comando in comandos:
    print(f"\n iniciando execução do comando {comando}!")
    processo = subprocess.Popen(comando, shell=True)
    print(f"comando {comando} executado com sucesso! \n")
    processo.wait()  # Aguardar o término do processo

print("Todos os comandos foram executados.")
