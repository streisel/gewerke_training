import argparse
import os
import re

def is_valid_gewerk(gewerk):
    """
    Prüft, ob ein Gewerk-Eintrag gültig ist.
    :param gewerk: Der zu prüfende Gewerk-Eintrag.
    :return: True, wenn der Eintrag gültig ist, False ansonsten.
    """
    # Entferne Einträge, die nur aus Ziffern bestehen
    if re.match(r"^\d+$", gewerk):
        return False

    # Entferne Einträge, die hauptsächlich aus Ziffern und wenigen Sonderzeichen bestehen
    if re.match(r"^[^a-zA-Z]*\d+[^a-zA-Z]*$", gewerk):
        return False

    # Entferne sehr kurze Einträge (z. B. Ein-Buchstaben-Einträge)
    if len(gewerk) < 3:
        return False

    # Einträge mit sinnvollen Sonderzeichen (z. B. ".winterdienst") behalten
    return True

def clean_gewerke(input_file, output_file):
    """
    Bereinigt die Gewerkeliste und speichert die standardisierten Einträge.
    
    :param input_file: Pfad zur Eingabedatei mit rohen Gewerken.
    :param output_file: Pfad zur Ausgabedatei für bereinigte Gewerke.
    """
    try:
        # Einträge lesen
        with open(input_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # Bereinigung
        cleaned = set()  # Set für Duplikateliminierung
        for line in lines:
            gewerk = line.strip().lower()  # Groß-/Kleinschreibung normalisieren
            if gewerk and is_valid_gewerk(gewerk):  # Filter anwenden
                cleaned.add(gewerk)

        # Sortierte Liste speichern
        with open(output_file, "w", encoding="utf-8") as f:
            for gewerk in sorted(cleaned):
                f.write(gewerk + "\n")

        print(f"Bereinigung abgeschlossen. Ergebnisse in {output_file}")

    except Exception as e:
        print(f"Fehler bei der Verarbeitung: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bereinigt eine Gewerkeliste.")
    parser.add_argument("input_file", help="Pfad zur Eingabedatei (z. B. output.txt)")
    parser.add_argument("output_file", help="Pfad zur Ausgabedatei (z. B. cleaned_output.txt)")

    args = parser.parse_args()

    clean_gewerke(args.input_file, args.output_file)
