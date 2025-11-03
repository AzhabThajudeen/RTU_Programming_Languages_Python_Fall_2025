"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# Create the datasets
temperatures = [22, 25, 18, 19, 21, 23, 24]  # Example temperatures for one week
city_population = {
    "New York": 8419600,
    "Los Angeles": 3980400,
    "Chicago": 2716000,
    "Houston": 2328000,
    "Phoenix": 1690000
}

# Compute aggregates
# 1. Calculate the average temperature
average_temperature = sum(temperatures) / len(temperatures)

# 2. Find the city with the largest population
largest_city = max(city_population, key=city_population.get) # type: ignore
largest_population = city_population[largest_city]

# 3. Calculate the total population of all cities
total_population = sum(city_population.values())

# Print results
print(f"Average temperature: {average_temperature:.2f}°C")
print(f"Largest city: {largest_city} - {largest_population} people")
print(f"Total population: {total_population} people")
