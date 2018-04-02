import sqlite3

db_url = 'mileage.db'

"""
    Before running this test, create test_miles.db
    Create expected miles table
    create table miles (vehicle text, total_miles float);
"""

class Error_miles(Exception):
    pass

def add_miles(vehicle, new_miles):
    """If the vehicle is in the database, increment the number of miles by new_miles
    If the vehicle is not in the database, add the vehicle and set the number of miles to new_miles
    If the vehicle is None or new_miles is not a positive number, raise MileageError"""
    #vehicle = all_chars_upper_case(vehicle)

    if not vehicle:
        raise Error_miles('Provide a vehicle name')

    if not isinstance(new_miles, (int, float)) or new_miles < 0:
        raise Error_miles('Provide a positive number for new miles')

    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    rows_mod = cursor.execute('UPDATE MILES SET total_miles = total_miles + ? WHERE vehicle = ?', (new_miles, vehicle))
    if rows_mod.rowcount == 0:
        cursor.execute('INSERT INTO MILES VALUES (?, ?)', (vehicle, new_miles))
    conn.commit()
    conn.close()

def miles_upper_case(vehicle):

    return string.upper()

def get_mileage(vehicle):

    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    results = cursor.execute('SELECT total_miles FROM MILES WHERE vehicle = ?', (vehicle,)).fetchall()

    if len(results) is 1:
        return str(results[0][0])
        return None

def main():
    while True:
        vehicle = input("Find mileage by vehicle:\nPress 'q' to exit:\n")
        if vehicle == 'q':
            break

        miles = int(input('Enter new miles for %s ' % vehicle)) ## TODO input validation
        vehicle = miles_upper_case(vehicle)
        add_miles(vehicle, miles)
        get_mileage(vehicle)


if __name__ == '__main__':
    main()
