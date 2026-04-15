# travail-pratique-cybersecuriter-python-



# Simulation du modèle OSI

# ---------------- ENCAPSULATION ----------------

def application(data):
    print("Application :", data)
    return data

def presentation(data):
    data = "[ENCODE]" + data
    print("Présentation :", data)
    return data

def session(data):
    data = "[SESSION]" + data
    print("Session :", data)
    return data

def transport(data):
    data = "[PORT:8080]" + data
    print("Transport :", data)
    return data

def reseau(data):
    data = "[IP:192.168.1.1]" + data
    print("Réseau :", data)
    return data

def liaison(data):
    data = "[MAC:AA:BB:CC:DD]" + data
    print("Liaison :", data)
    return data

def physique(data):
    data = "[BITS]" + data
    print("Physique :", data)
    return data


# ---------------- DÉCAPSULATION ----------------

def decapsulation(data):
    print("\n--- Décapsulation ---")

    data = data.replace("[BITS]", "")
    print("Physique supprimée :", data)

    data = data.replace("[MAC:AA:BB:CC:DD]", "")
    print("Liaison supprimée :", data)

    data = data.replace("[IP:192.168.1.1]", "")
    print("Réseau supprimé :", data)

    data = data.replace("[PORT:8080]", "")
    print("Transport supprimé :", data)

    data = data.replace("[SESSION]", "")
    print("Session supprimée :", data)

    data = data.replace("[ENCODE]", "")
    print("Présentation supprimée :", data)

    print("\nMessage final reçu :", data)


# ---------------- PROGRAMME PRINCIPAL ----------------

message = "Bonjour"

print("=== ENCAPSULATION ===\n")

data = application(message)
data = presentation(data)
data = session(data)
data = transport(data)
data = reseau(data)
data = liaison(data)
data = physique(data)

print("\nDonnées envoyées :", data)

# Décapsulation
decapsulation(data)
