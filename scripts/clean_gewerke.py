import argparse
import os

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
            if gewerk and gewerk not in ["-", "n/a"]:  # Müll und leere Zeilen entfernen
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
