from colorama import init, Fore, Back, Style
import json
import os

# Initialisierung der Farben
init(autoreset=True)

def wahle():
    print(Fore.YELLOW + "Wähle Aktion:" + Style.RESET_ALL)

def save(data):
# Speichert die Liste der Ausgaben in einer JSON-Datei
    with open("ausgaben.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def load():
# Lädt die Ausgaben aus einer JSON-Datei. Wenn die Datei nicht existiert, wird eine leere Liste zurückgegeben
    if os.path.exists("ausgaben.json"):
        try:
            with open("ausgaben.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except:
            print(Fore.BLACK + Back.RED + "❌ Fehler beim Lesen der Datei. Wir beginnen von vorne." + Style.RESET_ALL)
            return []
    return []

def Kostenberechnung():
    print(Fore.BLACK + Back.YELLOW + "=== Kostenberechnung ===" + Style.RESET_ALL)

    ausgaben = load() #Gespeicherte Daten laden

    while True:
        wahle()
        print(Fore.GREEN + '1. Ausgabe hinzufügen' + '\n2. Alles anzeigen' + '\n3. Ausgabe löschen' + '\n4. Beenden' + Style.RESET_ALL)

        wahl = input(Fore.BLACK + Back.CYAN + "Ihre Aktion" + Style.RESET_ALL)

        if wahl not in ["1", "2", "3", "4"]:
            print(Back.RED + Fore.BLACK + "❌ Fehler: Falscher Wert bitte versuchen Sie es noch einmal." + Style.RESET_ALL)
            continue

        elif wahl == "1":
            while True:
                try:
                    wie_viel = float(input(Fore.BLACK + Back.WHITE + "Wie viel? " + Style.RESET_ALL).replace(',', '.'))
                    kategorie = input(Fore.BLACK + Back.WHITE + "Kategorie?" + Style.RESET_ALL).lower().strip()
                    if not kategorie:
                        print(Fore.BLACK + Back.RED + "❌ Fehler: Sie haben nichts eingegeben." + Style.RESET_ALL)
                        continue
                    else:
                        ausgaben.append([wie_viel, kategorie])
                        save(ausgaben)  # Nach jeder Ausgabe speichern
                        print(Fore.BLACK + Back.GREEN + '✅ Erfolgreich gespeichert!' + Style.RESET_ALL)
                    break
                except ValueError:
                    print(Back.RED + Fore.BLACK + "❌ Fehler: Geben Sie bitte eine gültige Zahl ein." + Style.RESET_ALL)

        elif wahl == "2":
            if not ausgaben:
                print(Fore.BLACK + Back.RED + "Noch keine Ausgaben vorhanden." + Style.RESET_ALL)
                continue

            gesamt = 0
            print(Fore.BLACK + Back.GREEN + "--- Alle Ausgaben ---" + Style.RESET_ALL)

            for ausgabe in ausgaben:
                print("Summe:",ausgabe[0],"€", "Kategorie:", ausgabe[1].title())
                gesamt += ausgabe[0]
            print(Fore.BLACK + Back.GREEN + "Insgesamt:", gesamt,"€" + Style.RESET_ALL)

        elif wahl == "3":
                if not ausgaben:
                    print(Fore.BLACK + Back.RED + "Noch keine Ausgaben vorhanden." + Style.RESET_ALL)
                    continue

                print(Fore.BLACK + Back.YELLOW + "--- Alle Ausgaben ---" + Style.RESET_ALL)
                for i, ausgabe in enumerate(ausgaben, start=1):
                    print(Fore.LIGHTCYAN_EX + f"{i}. Kategorie: {ausgabe[1].title()} | Summe: {ausgabe[0]} €" + Style.RESET_ALL)
                while True:
                    try:
                        index = int(input(Fore.LIGHTYELLOW_EX + "Welche Nummer löschen?:" + Style.RESET_ALL)) - 1
                        if 0 <= index < len(ausgaben):
                            sicher = input(Fore.RED + "Sicher?(Ja/Nein):" + Style.RESET_ALL).lower()
                            if sicher == "ja":
                                geloscht = ausgaben.pop(index)
                                save(ausgaben)
                                print(Fore.BLACK + Back.LIGHTGREEN_EX + f"Erfolgreich gelöscht: {geloscht[1].title()} ({geloscht[0]} €) und gespeichert" + Style.RESET_ALL)
                                break
                            elif sicher == "nein":
                                print(Fore.RED + "Abgebrochen." + Style.RESET_ALL)
                                break
                            else:
                                print(Fore.RED + "❌ Falscher Wert. Bitte 'ja' oder 'nein' eingeben." +  Style.RESET_ALL)
                        else:
                            print(Fore.RED + "❌ Diese Nummer existiert nicht im System." +  Style.RESET_ALL)
                    except ValueError:
                        print(Fore.RED + "❌ Bitte geben Sie eine gültige Nummer ein!" +  Style.RESET_ALL)

        elif wahl == "4":
            while True:
                sicher = input(Fore.RED + "Sicher?(Ja/Nein):" + Style.RESET_ALL).lower()
                if sicher == "ja":
                    print(Fore.BLACK + Back.RED + "Tschüss!" + Style.RESET_ALL)
                    return
                elif sicher == "nein":
                    print(Fore.MAGENTA + "Zurück zum Hauptmenü." + Style.RESET_ALL)
                    break
                else:
                    print(Fore.BLACK + Back.RED + "❌ Falscher Wert, bitte versuchen Sie es noch einmal." + Style.RESET_ALL)

if __name__ == "__main__":
    Kostenberechnung()

