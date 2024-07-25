def adjust_signal_time(vehicle_count_file="vehicle_count.txt"):
    base_green_time = 30  # base green light time in seconds
    vehicle_multiplier = 2  # additional seconds per detected vehicle

    try:
        with open(vehicle_count_file, "r") as file:
            vehicle_count = int(file.read().strip())
            adjusted_green_time = base_green_time + (vehicle_multiplier * vehicle_count)
            print(f"Adjusted green signal time: {adjusted_green_time} seconds")
    except FileNotFoundError:
        print(f"Error: {vehicle_count_file} not found.")
    except ValueError:
        print(f"Error: Invalid vehicle count in {vehicle_count_file}.")

if __name__ == "__main__":
    adjust_signal_time()
