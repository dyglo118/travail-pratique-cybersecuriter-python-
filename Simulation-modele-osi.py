import time

def pause():
    time.sleep(1)

def encapsulation(message):
    print("\n--- ENCAPSULATION ---\n")

    # Application
    print("Couche Application : préparation du message")
    print("Données :", message)
    pause()

    # Présentation
    message = "[ENCODE]" + message
    print("\nCouche Présentation : encodage des données")
    print("Ajout : [ENCODE]")
    print("Résultat :", message)
    pause()

    # Session
    message = "[SESSION:1234]" + message
    print("\nCouche Session : ouverture d'une session")
    print("Session ID : 1234")
    print("Résultat :", message)
    pause()

    # Transport
    message = "[PORT:8080]" + message
    print("\nCouche Transport : ajout du port")
    print("Port : 8080")
    print("Résultat :", message)
    pause()

    # Réseau
    message = "[IP:192.168.1.1]" + message
    print("\nCouche Réseau : ajout de l'adresse IP")
    print("Adresse IP : 192.168.1.1")
    print("Résultat :", message)
    pause()

    # Liaison
    message = "[MAC:AA:BB:CC:DD:EE:FF]" + message
    print("\nCouche Liaison : ajout de l'adresse MAC")
    print("Adresse MAC : AA:BB:CC:DD:EE:FF")
    print("Résultat :", message)
    pause()

    # Physique
    message = "[BITS]" + message
    print("\nCouche Physique : transformation en bits")
    print("Ajout : [BITS]")
    print("Résultat final :", message)
    pause()

    return message


def decapsulation(message):
    print("\n--- DECAPSULATION ---\n")

    couches = [
        ("Physique", "[BITS]"),
        ("Liaison", "[MAC:AA:BB:CC:DD:EE:FF]"),
        ("Réseau", "[IP:192.168.1.1]"),
        ("Transport", "[PORT:8080]"),
        ("Session", "[SESSION:1234]"),
        ("Présentation", "[ENCODE]"),
    ]

    for nom, tag in couches:
        print(f"Couche {nom} : suppression des informations")
        message = message.replace(tag, "", 1)
        print("Supprimé :", tag)
        print("Résultat :", message)
        pause()

    print("\nCouche Application : récupération du message original")
    return message


def main():
    print("=== Simulation du modèle OSI ===\n")

    message = input("Inscrivez votre message : ")

    print("\nMessage initial :", message)

    message_encapsule = encapsulation(message)

    print("\nMessage encapsulé complet :")
    print(message_encapsule)

    message_final = decapsulation(message_encapsule)

    print("\nMessage final après décapsulation :")
    print(message_final)


if __name__ == "__main__":
    main()
