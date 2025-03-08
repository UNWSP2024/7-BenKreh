#Ben Krehbiel
#3/7/2025
#population, undefined

def population_statistics():
    pop_data = []  

    
    while True:
        try:
            year = int(input("Enter year (or -1 to stop): "))
            if year == -1:
                break

            state = input("Enter state name: ").strip()
            population = int(input("Enter population: "))

            if population < 0:
                print("This isn't the death count.")
            else:
                pop_data.append([year, state, population])

        except ValueError:
            print("Invalid input")

    
    get_year = int(input("\nEnter a year to see total population: "))
    sort_data = [entry for entry in pop_data if entry[0] == get_year]

    if not sort_data:
        print(f"No data found for {get_year}.")
        return

    
    total_population = sum(entry[2] for entry in sort_data)

    
    print(f"\nTotal population for {get_year}: {total_population:,}")



population_statistics()
