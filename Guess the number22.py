import random

def luaj_guess_number():
    numri_sekret = random.randint(1, 100)
    shancet_totale = 10
    tentativa = 0
    
    print("=" * 30)
    print("🎯 MIRËSEVINI NË GUESS THE NUMBER")
    print(f"Keni {shancet_totale} shance për të gjetur numrin (1-100).")
    print("=" * 30)

    while tentativa < shancet_totale:
        shancet_mbetura = shancet_totale - tentativa
        print(f"\nShancet e mbetura: {shancet_mbetura}")
        
        try:
            input_user = input("Shkruaj numrin tënd (ose 'q' për t'u larguar): ")
            
            if input_user.lower() == 'q':
                print("Lojë e ndërprerë. Shihemi herën tjetër!")
                return

            prova = int(input_user)
            tentativa += 1

            if prova < 1 or prova > 100:
                print("⚠️ Kujdes! Numri duhet të jetë midis 1 dhe 100.")
                continue

            if prova < numri_sekret:
                print("Më lart! ⬆️")
            elif prova > numri_sekret:
                print("Më poshtë! ⬇️")
            else:
                print(f"\n🎉 BRAVO ALAN! E gjete me {tentativa} tentativa!")
                print(f"Numri ishte vërtet {numri_sekret}.")
                break

        except ValueError:
            print("❌ Gabim! Shkruaj një numër të vlefshëm.")

    if tentativa == shancet_totale and prova != numri_sekret:
        print("\n" + "!" * 30)
        print(f"LOJA MBAROI! Nuk ke më shance. 💀")
        print(f"Numri sekret ishte: {numri_sekret}")
        print("!" * 30)

if __name__ == "__main__":
    luaj_guess_number()