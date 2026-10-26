from datetime import datetime

from pda_general import *

####################emfanizei to menu tou estiatoriou me ta fagita/pota

def checker_empty_tables():
    if tables == [[[], [], []], [[], [], []], [[], [], []]]:
        input("[ℹ️] Δεν υπάρχει ενεργή παραγγελία!\n[⬅️] Πάτησε 0 για επιστροφή στο μενού ")
        return True

def show_menu():
    print("""
    ╔══════════════════════════════════════════╗
    ║                                          ║
    ║            PDA ΕΣΤΙΑΤΟΡΙΟΥ               ║
    ║           Κ Α Τ Α Λ Ο Γ Ο Σ              ║
    ║                                          ║
    """)
    for i in range(len(items)):
        print("           ", items[i])

    input("\n[⬅️] Πάτησε 0 για επιστροφή στο μενού. ")

####################elegxei an o aritmos einai apo x mexri y & kanei elegxw gia ta grammata

def request_number(minimum,maximum,message):
    select = input(message)

    while not select.isdigit() or int(select) > maximum or int(select) < minimum:
        select = input(message)

    return int(select)

###################elegxei ta diathesima trapezia me enan pseutiko arithmiti (numbers_tables), raw/col 3*3 pinaka

def tables_show():
    print("""
    ╔══════════════════════════════════════╗
    ║           PDA ΕΣΤΙΑΤΟΡΙΟΥ            ║
    ║          ΔΙΑΘΕΣΙΜΑ ΤΡΑΠΕΖΙΑ          ║
    ╠══════════════════════════════════════╣
    ║                                      ║
    """)
    numbers_tables = 1
    for i in range(len(tables)):
        for j in range(len(tables[i])):
            if tables[i][j] == []:
                print("            Τραπέζι ", numbers_tables, ": ✅ Ελεύθερο")
            numbers_tables += 1

    print("""
    ║                                      ║                     
    ╚══════════════════════════════════════╝
    """)

###################paraggelia kai kleisimo trapeziou

def new_table_reserve():
    tables_show()
    while True:
        choose_table = request_number(1,9,"[🔔] Ποιο τραπέζι θέλεις να επιλέξεις [1-9]; ")

        i = (int(choose_table) - 1) // 3
        j = (int(choose_table) - 1) % 3

        if tables[i][j] != []:
            print("[❌] Το τραπέζι δεν είναι διαθέσιμο.")
        else:
            break

    pda_show_table_menu()
    total = 0.0
    while True:
        choose_item = request_number(0, 8, "[🔔] Επίλεξε το προϊόν που θέλεις να προσθέσεις [1-8] \n[⬅️] Πάτησε 0 για επιστροφή στο μενού ")
        if choose_item == 0:
            break
        else:
            quantity = int(input("[🔔] Πόσα τεμάχια θέλεις να προσθέσεις; "))
            for q in range(quantity):
                tables[i][j].append(items[choose_item - 1])
                total += price[choose_item - 1]

        tables_money[i][j] = total

def show_items_per_table():
    if checker_empty_tables() == True:
        return

    print("""
    ╔══════════════════════════════════════╗
    ║           PDA ΕΣΤΙΑΤΟΡΙΟΥ            ║
    ║          ΠΡΟΒΟΛΗ ΠΑΡΑΓΓΕΛΙΑΣ         ║
    ╠══════════════════════════════════════╣
    ║                                      ║
    """)
    numbers_tables = 1
    for i in range(len(tables)):
        for j in range(len(tables[i])):
            if tables[i][j] != []:
                print("          Τραπέζι ", numbers_tables, ": 🍽️ Σε εξυπηρέτηση")
            numbers_tables += 1

    print("""
    ║                                      ║                     
    ╚══════════════════════════════════════╝
    """)
    while True:
        choose_table = request_number(1, 9, "[🔔] Επίλεξε ένα τραπέζι για να δεις την παραγγελία του. ")

        i = (int(choose_table) - 1) // 3
        j = (int(choose_table) - 1) % 3

        if tables[i][j] == []:
            print("[❌] Το τραπέζι είναι ελεύθερο.")
        else:
            break

    print("""
    ╔══════════════════════════════════════╗
    ║           PDA ΕΣΤΙΑΤΟΡΙΟΥ            ║
    ║          ΠΡΟΒΟΛΗ ΠΑΡΑΓΓΕΛΙΑΣ         ║
    ╠══════════════════════════════════════╣
    ║                                      ║
    """)

    for g in range(len(tables[i][j])):
        print("            ",tables[i][j][g])

    print("""
    ║                                      ║
    ╠══════════════════════════════════════╣
       🧾 ΣΥΝΟΛΟ:                 """, tables_money[i][j],"€")
    input("\n[⬅️] Πάτησε 0 για επιστροφή στο μενού. ")


def add_more_items_per_table(): #sorry gia to repeat
    if checker_empty_tables() == True:
        return

    while True:

        print("""
        ╔══════════════════════════════════════╗
        ║           PDA ΕΣΤΙΑΤΟΡΙΟΥ            ║
        ║          ΠΡΟΒΟΛΗ ΠΑΡΑΓΓΕΛΙΑΣ         ║
        ╠══════════════════════════════════════╣
        ║                                      ║
        """)
        numbers_tables = 1
        for i in range(len(tables)):
            for j in range(len(tables[i])):
                if tables[i][j] != []:
                    print("              Τραπέζι ", numbers_tables, ": 🍽️ Σε εξυπηρέτηση")
                numbers_tables += 1

        print("""
        ║                                      ║                     
        ╚══════════════════════════════════════╝
        """)
        while True:
            choose_table = request_number(1, 9, "[🔔] Επίλεξε ένα τραπέζι για την προσθήκη προϊόντος ")

            i = (int(choose_table) - 1) // 3
            j = (int(choose_table) - 1) % 3

            if tables[i][j] == []:
                print("[❌] Το τραπέζι είναι ελεύθερο.")
            else:
                break

        pda_show_table_menu()
        plus_total = 0.0
        choose_item = request_number(0, 8,
                                     "[🔔] Επίλεξε το προϊόν που θέλεις να προσθέσεις [1-8] \n[⬅️] Πάτησε 0 για επιστροφή στο μενού ")
        if choose_item == 0:
            break
        else:
            quantity = int(input("[🔔] Πόσα τεμάχια θέλεις να προσθέσεις; "))
            for q in range(quantity):
                tables[i][j].append(items[choose_item - 1])
                plus_total += price[choose_item - 1]

        tables_money[i][j] += plus_total
        print("[✅] Τα προϊόντα προστέθηκαν με επιτυχία!")
        input("[⬅️] Πάτησε 0 για επιστροφή στο μενού. ")
        break


def remove_more_items_per_table(): #sorry gia to repeat
    if checker_empty_tables() == True:
        return

    while True:

        print("""
        ╔══════════════════════════════════════╗
        ║           PDA ΕΣΤΙΑΤΟΡΙΟΥ            ║
        ║          ΠΡΟΒΟΛΗ ΠΑΡΑΓΓΕΛΙΑΣ         ║
        ╠══════════════════════════════════════╣
        ║                                      ║
        """)
        numbers_tables = 1
        for i in range(len(tables)):
            for j in range(len(tables[i])):
                if tables[i][j] != []:
                    print("              Τραπέζι ", numbers_tables, ": 🍽️ Σε εξυπηρέτηση")
                numbers_tables += 1

        print("""
        ║                                      ║                     
        ╚══════════════════════════════════════╝
        """)
        while True:
            choose_table = request_number(0, 9, "[🔔] Επίλεξε ένα τραπέζι για την αφαίρεση προϊόντος\n[⬅️] Πάτησε 0 για επιστροφή στο μενού ")

            if choose_table == 0:
                return

            i = (choose_table - 1) // 3
            j = (choose_table - 1) % 3

            if tables[i][j] == []:
                print("[❌] Το τραπέζι είναι ελεύθερο.")
            else:
                break

        num = 1
        print("""
        ╔══════════════════════════════════════╗
        ║           PDA ΕΣΤΙΑΤΟΡΙΟΥ            ║
        ║          ΠΡΟΒΟΛΗ ΠΑΡΑΓΓΕΛΙΑΣ         ║
        ╠══════════════════════════════════════╣
        ║                                      ║
        """)

        for g in range(len(tables[i][j])):
            print("                ", f"{num}.", tables[i][j][g])
            num += 1

        print("""
        ║                                      ║
        ╠══════════════════════════════════════╣
           🧾 ΣΥΝΟΛΟ:                 """, tables_money[i][j], "€")

        while tables[i][j]:
            choose_item = request_number(0, len(tables[i][j]), f"[🔔] Επίλεξε το προϊόν που θέλεις να αφαιρέσεις. [1-{len(tables[i][j])}]\n[⬅️] Πάτησε 0 για επιστροφή στο μενού ")

            if choose_item == 0:
                return

            removed_item = tables[i][j].pop(choose_item - 1)
            tables_money[i][j] -= price[items.index(removed_item)]

            print("[✅] Το προϊόν αφαιρέθηκε με επιτυχία!")
            print(tables)
            print(tables_money)

        if not tables[i][j]:
            tables_money[i][j] = 0.0
            print("[❌] Το τραπέζι είναι πλέον ελεύθερο.")

def total_price():
    if checker_empty_tables() == True:
        return

    while True:
        print("""
        ╔══════════════════════════════════════╗
        ║           PDA ΕΣΤΙΑΤΟΡΙΟΥ            ║
        ║        ΥΠΟΛΟΓΙΣΜΟΣ ΛΟΓΑΡΙΑΣΜΟΥ       ║
        ╠══════════════════════════════════════╣
        ║                                      ║
        """)
        numbers_tables = 1
        for i in range(len(tables)):
            for j in range(len(tables[i])):
                if tables[i][j] != []:
                    print("              Τραπέζι ", numbers_tables, ": 🍽️ Σε εξυπηρέτηση")
                numbers_tables += 1

        print("""
        ║                                      ║                     
        ╚══════════════════════════════════════╝
        """)
        while True:
            choose_table = request_number(0, 9,
                                          "[🔔] Επίλεξε τραπέζι για τον υπολογισμό του λογαριασμού.\n[⬅️] Πάτησε 0 για επιστροφή στο μενού ")

            if choose_table == 0:
                return

            i = (choose_table - 1) // 3
            j = (choose_table - 1) % 3

            if tables[i][j] == []:
                print("[❌] Το τραπέζι είναι ελεύθερο.")
            else:
                print(f"[🧾] Ο συνολικός λογαριασμός είναι {tables_money[i][j]:.2f}€.")
                input("[⬅️] Πάτησε 0 για επιστροφή στο μενού ")
                return

def payment_method():
    if checker_empty_tables() == True:
        return
    print(payments_meth)

    while True:
        print("""
        ╔══════════════════════════════════════╗
        ║           PDA ΕΣΤΙΑΤΟΡΙΟΥ            ║
        ║        ΥΠΟΛΟΓΙΣΜΟΣ ΛΟΓΑΡΙΑΣΜΟΥ       ║
        ╠══════════════════════════════════════╣
        ║                                      ║
        """)
        numbers_tables = 1
        for i in range(len(tables)):
            for j in range(len(tables[i])):
                if tables[i][j] != []:
                    print("              Τραπέζι ", numbers_tables, ": 🍽️ Σε εξυπηρέτηση")
                numbers_tables += 1

        print("""
        ║                                      ║                     
        ╚══════════════════════════════════════╝
        """)
        while True:
            choose_table = request_number(0, 9,
                                          "[🔔] Επίλεξε τραπέζι για τον υπολογισμό του λογαριασμού.\n[⬅️] Πάτησε 0 για επιστροφή στο μενού ")

            if choose_table == 0:
                return

            i = (choose_table - 1) // 3
            j = (choose_table - 1) % 3

            if tables[i][j] == []:
                print("[❌] Το τραπέζι είναι ελεύθερο.")
            else:
                choose_method = request_number(1, 2,"[💳] Επίλεξε τρόπο πληρωμής: \n1. 💳 Κάρτα \n2. 💵 Μετρητά ")
                if choose_method == 1:
                    print("[✅] Επιλέχθηκε πληρωμή με κάρτα.")
                    payments_meth[i][j][0] = "Κάρτα"
                else:
                    print("[✅] Επιλέχθηκε πληρωμή με μετρητά.")
                    payments_meth[i][j][0] = "Μετρητά"

def show_full_info_about_table():
    if checker_empty_tables() == True:
        return

    while True:
        print("""
        ╔══════════════════════════════════════╗
        ║           PDA ΕΣΤΙΑΤΟΡΙΟΥ            ║
        ║        ΥΠΟΛΟΓΙΣΜΟΣ ΛΟΓΑΡΙΑΣΜΟΥ       ║
        ╠══════════════════════════════════════╣
        ║                                      ║
        """)
        numbers_tables = 1
        for i in range(len(tables)):
            for j in range(len(tables[i])):
                if tables[i][j] != []:
                    print("              Τραπέζι ", numbers_tables, ": 🍽️ Σε εξυπηρέτηση")
                numbers_tables += 1

        print("""
        ║                                      ║                     
        ╚══════════════════════════════════════╝
        """)
        while True:
            choose_table = request_number(0, 9,
                                          "[🔔] Επίλεξε τραπέζι για προβολή των πληροφοριών του.\n[⬅️] Πάτησε 0 για επιστροφή στο μενού ")

            if choose_table == 0:
                return

            i = (choose_table - 1) // 3
            j = (choose_table - 1) % 3

            if tables[i][j] == []:
                print("[❌] Το τραπέζι είναι ελεύθερο.")
            else:
                time = datetime.now().strftime("%H:%M")
                print(f"""
        ╔══════════════════════════════════════╗
        ║          ΠΛΗΡΟΦΟΡΙΕΣ ΤΡΑΠΕΖΙΟΥ       ║
        ╠══════════════════════════════════════╣
        ║  🔢 Τραπέζι: {choose_table}          
        ║  🍽️ Κατάσταση: Κατειλημμένο          
        ║  🕒 Ώρα παραγγελίας: {time}          
        ║  🧾 Προϊόντα: {len(tables[i][j])}    
        ║  💰 Σύνολο: {tables_money[i][j]}€    
        ║  💳 Πληρωμή: {payments_meth[i][j]}   
        ║  ⏳ Εξόφληση: Εκκρεμεί               
        ╚══════════════════════════════════════╝
                """)

def all_tables_showed():
    if checker_empty_tables() == True:
        return


    print("""
    ╔══════════════════════════════════════╗
    ║           PDA ΕΣΤΙΑΤΟΡΙΟΥ            ║
    ║           ΟΛΑ ΤΑ ΤΡΑΠΕΖΙΑ            ║
    ╠══════════════════════════════════════╣
    ║                                      ║
    """)
    numbers_tables = 1
    for i in range(len(tables)):
        for j in range(len(tables[i])):
            if tables[i][j] == []:
                print("            Τραπέζι ", numbers_tables, ": ✅ Ελεύθερο")
            else:
                print("            Τραπέζι ", numbers_tables, ": 🔴 Κατειλημμένο")
            numbers_tables += 1

    print("""
    ║                                      ║                     
    ╚══════════════════════════════════════╝
    """)

    input("\n[⬅️] Πάτησε 0 για επιστροφή στο μενού. ")

def close_table():
    if checker_empty_tables() == True:
        return

    while True:

        print("""
        ╔══════════════════════════════════════╗
        ║           PDA ΕΣΤΙΑΤΟΡΙΟΥ            ║
        ║          ΚΛΕΙΣΙΜΟ ΤΡΑΠΕΖΙΟΥ          ║
        ╠══════════════════════════════════════╣
        ║                                      ║
        """)
        numbers_tables = 1
        for i in range(len(tables)):
            for j in range(len(tables[i])):
                if tables[i][j] != []:
                    print("              Τραπέζι ", numbers_tables, ": 🍽️ Σε εξυπηρέτηση")
                numbers_tables += 1

        print("""
        ║                                      ║                     
        ╚══════════════════════════════════════╝
        """)
        while True:
            choose_table = request_number(0, 9, "[🔔] Επίλεξε τραπέζι για κλείσιμο.\n[⬅️] Πάτησε 0 για επιστροφή στο μενού ")

            if choose_table == 0:
                return

            i = (choose_table - 1) // 3
            j = (choose_table - 1) % 3

            if tables[i][j] == []:
                print("[❌] Το τραπέζι είναι ηδη ελεύθερο.")
            else:
                tables[i][j] = []
                payments_meth[i][j] = "Χωρίς τρόπο πληρωμής"
                tables_money[i][j] = 0.0
                print("[✅] Το τραπέζι είναι πλέον καθαρό!")
                return

