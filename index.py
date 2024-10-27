def maximize_holidays(offices_within_range, holidays):
    max_moves_per_quarter = 2
    max_moves_per_year = 8
    quarters = 4
    total_holidays = 0
    office_transitions = []
    
    # Function to calculate holidays for a given office
    def get_holidays_for_office(office):
        return holidays[office]

    # Function to find the optimal office transition
    def find_best_office(current_office, month):
        best_office = current_office
        max_holidays = get_holidays_for_office(current_office)[month]
        
        # Check reachable offices
        for neighbor in offices_within_range[current_office]:
            current_holidays = get_holidays_for_office(neighbor)[month]
            if current_holidays > max_holidays:
                max_holidays = current_holidays
                best_office = neighbor

        return best_office, max_holidays

    # Start with any office, for example "Noida"
    current_office = "Noida"
    current_quarter_moves = 0
    current_year_moves = 0
    month = 0

    while month < 12:
        quarter_index = month // 3

        # Get best office for the current month
        best_office, max_holidays = find_best_office(current_office, month)

        # Check if we can move
        if best_office != current_office:
            if current_quarter_moves < max_moves_per_quarter and current_year_moves < max_moves_per_year:
                office_transitions.append(best_office)
                current_office = best_office
                current_quarter_moves += 1
                current_year_moves += 1

        # Add holidays from the current office
        total_holidays += get_holidays_for_office(current_office)[month]
        month += 1

        # Reset quarter moves at the end of each quarter
        if month % 3 == 0:
            current_quarter_moves = 0

    return office_transitions, total_holidays


# Example data
offices_within_range = {
    "Noida": ["Delhi", "Gurugram", "Faridabad"],
    "Delhi": ["Noida", "Gurugram", "Sonipat", "Faridabad"],
    "Sonipat": ["Delhi", "Panipat", "Gurugram"],
    "Gurugram": ["Noida", "Delhi", "Sonipat", "Panipat", "Faridabad"],
    "Panipat": ["Sonipat", "Gurugram"],
    "Faridabad": ["Delhi", "Noida", "Gurugram"]
}

holidays = {
    "Noida": [1, 3, 4, 2, 1, 5, 6, 5, 1, 7, 2, 1],
    "Delhi": [5, 1, 8, 2, 1, 7, 2, 6, 2, 8, 2, 6],
    "Sonipat": [2, 5, 8, 2, 1, 6, 9, 3, 2, 1, 5, 7],
    "Gurugram": [6, 4, 1, 6, 3, 4, 7, 3, 2, 5, 7, 8],
    "Panipat": [2, 4, 3, 1, 7, 2, 6, 8, 2, 1, 4, 6],
    "Faridabad": [2, 4, 6, 7, 2, 1, 3, 6, 3, 1, 6, 8]
}

# Running the algorithm
transitions, total_holidays = maximize_holidays(offices_within_range, holidays)
print("Office Transitions:", transitions)
print("Total Holidays Enjoyed:", total_holidays)
