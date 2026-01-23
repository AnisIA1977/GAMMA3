import requests
import sys

BASE_URL = "http://127.0.0.1:8000"

def seed_data():
    print(f"Seeding data to {BASE_URL}...")

    # --- 1. Classes ---
    classes = [
        {"code": "1", "designation": "Matériel Mécanique"},
        {"code": "2", "designation": "Matériel Electronique"},
        {"code": "3", "designation": "Matériel d’armes et système d’armes"},
        {"code": "4", "designation": "Matériel Electrotechnique"},
        {"code": "5", "designation": "Matière d'œuvres"},
        {"code": "6", "designation": "Matériel de protection général et de plongée"},
        {"code": "7", "designation": "Matériel de quincaillerie générale"},
        {"code": "8", "designation": "Matériel d'équipement général de vie à bord"},
    ]

    class_ids = {} # Map code -> id

    for cls in classes:
        try:
            r = requests.post(f"{BASE_URL}/classes/", json=cls)
            if r.status_code == 200:
                print(f"Created Class: {cls['code']} - {cls['designation']}")
                class_ids[cls['code']] = r.json()['id']
            else:
                print(f"Skipped/Error Class {cls['code']}: {r.text}")
                # Try to get existing ID if it failed (likely exists)
                # Ideally we'd implement a get-by-code or just list all, but for simple seeding this is fine.
        except Exception as e:
            print(f"Error connecting: {e}")
            return

    # --- 2. SubClasses (For Class 1 - Mécanique) ---
    if "1" in class_ids:
        subclasses_1 = [
            {"code": "00", "designation": "Moteurs Diesels"},
            {"code": "05", "designation": "Réducteurs Inverseurs"},
            {"code": "10", "designation": "Lignes de Propulsion"},
            {"code": "15", "designation": "Compresseurs"},
            {"code": "20", "designation": "Pompes"},
            {"code": "25", "designation": "Installation Frigorifiques"},
            {"code": "30", "designation": "Groupes Hydrophores"},
            {"code": "35", "designation": "Unités de production d’eau"},
            {"code": "40", "designation": "Chaudières"},
            {"code": "45", "designation": "Turbines à gaz"},
            {"code": "50", "designation": "Système d’évacuation des eaux usées"},
        ]

        cid = class_ids["1"]
        for sub in subclasses_1:
            r = requests.post(f"{BASE_URL}/classes/{cid}/subclasses/", json=sub)
            if r.status_code == 200:
                print(f"  Created SubClass: {sub['code']}")
            else:
                print(f"  Error SubClass {sub['code']}: {r.text}")

    # --- 3. Constructors ---
    constructors = [
        {"code": "MT", "designation": "MTU"},
        {"code": "MW", "designation": "MWM"},
        {"code": "GM", "designation": "GM"},
        {"code": "CT", "designation": "CATERPILLAR"},
        {"code": "DZ", "designation": "DEUTZ"},
        {"code": "VP", "designation": "VOLVO PENTA"},
        {"code": "MN", "designation": "MAN"},
        {"code": "IV", "designation": "IVECO AIFO"},
        {"code": "BD", "designation": "BAUDOIN"},
        {"code": "DM", "designation": "DM GUSK SVES"},
        {"code": "LM", "designation": "LAMBARDINI"},
        {"code": "NR", "designation": "NORDBERG"},
        {"code": "PG", "designation": "PEGASO GUASCOR"},
        {"code": "ON", "designation": "ONAN"},
        {"code": "WB", "designation": "WESTER BEKE"},
    ]

    cons_ids = {}

    for cons in constructors:
        r = requests.post(f"{BASE_URL}/constructors/", json=cons)
        if r.status_code == 200:
            print(f"Created Constructor: {cons['code']}")
            cons_ids[cons['code']] = r.json()['id']
        else:
            print(f"Skipped/Error Constructor {cons['code']}: {r.text}")

    # --- 4. Series (For MTU) ---
    if "MT" in cons_ids:
        series_mtu = [
            {"code": "01", "designation": "20 V 538"},
            {"code": "02", "designation": "16 V 956"},
            {"code": "03", "designation": "12 V 493"},
            {"code": "04", "designation": "8/12 V 331 TC 92"},
            {"code": "05", "designation": "12/16 v 652"},
            {"code": "06", "designation": "8 v 4000M70"},
        ]

        cid = cons_ids["MT"]
        for ser in series_mtu:
            r = requests.post(f"{BASE_URL}/constructors/{cid}/series/", json=ser)
            if r.status_code == 200:
                print(f"  Created Series: {ser['code']}")
            else:
                print(f"  Error Series {ser['code']}: {r.text}")

    print("Seeding complete.")

if __name__ == "__main__":
    seed_data()
