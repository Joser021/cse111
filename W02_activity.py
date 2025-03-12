import math

def compute_volume(radius, height):
  return math.pi * radius**2 * height

def compute_surface_area(radius, height):
  return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(radius, height):
  return compute_volume(radius, height) / compute_surface_area(radius, height)

def compute_cost_efficiency(radius, height, price):
  return compute_volume(radius, height) / price

def main():
  name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short",
         "#10", "#211", "#300", "#303"]
  radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.4, 6.83, 15.72, 6.83, 7.62, 8.1]
  height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
  price = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

  max_cost_efficiency = 0
  max_cost_efficiency_index = -1
  max_storage_efficiency = 0
  max_storage_efficiency_index = -1

  for i in range(12):
    cost_efficiency = compute_cost_efficiency(radius[i], height[i], price[i])
    storage_efficiency = compute_storage_efficiency(radius[i], height[i])
    print(f"{name[i]} {compute_volume(radius[i], height[i]):.2f} "
          f"{compute_surface_area(radius[i], height[i]):.2f} "
          f"{compute_storage_efficiency(radius[i], height[i]):.2f} "
          f"{cost_efficiency}")
    if max_cost_efficiency < cost_efficiency:
      max_cost_efficiency = cost_efficiency
      max_cost_efficiency_index = i
    if max_storage_efficiency < storage_efficiency:
      max_storage_efficiency = storage_efficiency
      max_storage_efficiency_index = i
  print(f"The can with the maximum storage efficiency is {name[max_storage_efficiency_index]} with a storage efficiency of {max_storage_efficiency:.2f}")
  print(f"The can with the maximum cost efficiency is {name[max_cost_efficiency_index]} with a cost efficiency of {max_cost_efficiency:.2f}")

main()
