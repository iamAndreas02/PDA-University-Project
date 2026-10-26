from functions import *
from pda_general import *


def main():
    while True:
        pda_show_menu()
        selected_num = request_number(0,10, "[🔔] Δωσε εναν αριθμο απο το 0 μεχρι το 10: ")

        if selected_num == 1:
            show_menu()

        if selected_num == 2:
            new_table_reserve()

        if selected_num == 3:
            show_items_per_table()

        if selected_num == 4:
            add_more_items_per_table()

        if selected_num == 5:
            remove_more_items_per_table()

        if selected_num == 6:
            total_price()

        if selected_num == 7:
            payment_method()

        if selected_num == 8:
            show_full_info_about_table()

        if selected_num == 9:
            all_tables_showed()

        if selected_num == 10:
            close_table()

        if selected_num == 0:
            exit()

main()