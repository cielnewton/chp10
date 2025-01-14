import subprocess

# Fonction pour lire le fichier /var/log/auth.log avec une commande Linux
def read_auth_log():
    try:
        # Exécuter la commande cat pour lire le fichier
        result = subprocess.run(["sudo", "cat", "/var/log/auth.log"], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Erreur lors de la lecture du fichier :", e)
        return ""

# Fonction pour analyser les logs
def analyze_logs(log_data):
    # Diviser les logs en lignes
    lines = log_data.strip().split("\n")

    # Dictionnaires pour stocker les informations
    failed_ips = {}
    targeted_users = {}

    # Parcourir chaque ligne
    for line in lines:
        if "Failed password" in line:
            # Extraire l'utilisateur et l'adresse IP
            parts = line.split()
            user_index = parts.index("for") + 1
            ip_index = parts.index("from") + 1
            user = parts[user_index]
            ip = parts[ip_index]

            # Compter les occurrences des IPs
            if ip not in failed_ips:
                failed_ips[ip] = 0
            failed_ips[ip] += 1

            # Compter les occurrences des utilisateurs ciblés
            if user not in targeted_users:
                targeted_users[user] = 0
            targeted_users[user] += 1

    # Afficher les résultats
    print("Tentatives échouées par IP :")
    for ip, count in failed_ips.items():
        print(f"{ip} : {count} tentatives")

    print("\nUtilisateurs ciblés :")
    for user, count in targeted_users.items():
        print(f"{user} : {count} tentatives")

# Lire les logs
log_data = read_auth_log()

# Si des données ont été lues, les analyser
if log_data:
    analyze_logs(log_data)
else:
    print("Aucun log n'a été lu.")
