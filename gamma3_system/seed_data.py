import requests
import sys
import time

BASE_URL = "http://127.0.0.1:8000"

def seed_data():
    start_time = time.time()
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

    try:
        r = requests.post(f"{BASE_URL}/classes/bulk/", json=classes)
        if r.status_code == 200:
            for cls_data in r.json():
                print(f"Created Class: {cls_data['code']} - {cls_data['designation']}")
                class_ids[cls_data['code']] = cls_data['id']
        else:
            print(f"Error creating classes in bulk: {r.text}")
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
        r = requests.post(f"{BASE_URL}/classes/{cid}/subclasses/bulk/", json=subclasses_1)
        if r.status_code == 200:
            for sub_data in r.json():
                print(f"  Created SubClass: {sub_data['code']}")
        else:
            print(f"  Error SubClass bulk insert: {r.text}")

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

    r = requests.post(f"{BASE_URL}/constructors/bulk/", json=constructors)
    if r.status_code == 200:
        for cons_data in r.json():
            print(f"Created Constructor: {cons_data['code']}")
            cons_ids[cons_data['code']] = cons_data['id']
    else:
        print(f"Error creating constructors in bulk: {r.text}")

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
        r = requests.post(f"{BASE_URL}/constructors/{cid}/series/bulk/", json=series_mtu)
        if r.status_code == 200:
            for ser_data in r.json():
                print(f"  Created Series: {ser_data['code']}")
        else:
            print(f"  Error Series bulk insert: {r.text}")

    end_time = time.time()
    print(f"Seeding complete in {end_time - start_time:.4f} seconds.")

if __name__ == "__main__":
    seed_data()
