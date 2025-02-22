from datetime import datetime

# Define two dates
date1 = datetime(2025, 2, 22, 12, 0, 0)  # Example date 1
date2 = datetime(2025, 2, 20, 12, 0, 0)  # Example date 2

# Calculate the difference in seconds
difference_in_seconds = (date1 - date2).total_seconds()

# Print the result
print("Difference in seconds:", difference_in_seconds)
