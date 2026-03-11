import matplotlib.pyplot as plt
years = [2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]
temp = [24.89,25.01,25.37,25.26,25.11,25.05,24.9,24.09,25.2,26.15,27.4,26.8]
plt.plot(years,temp,marker='o')
plt.xlabel("Year")
plt.ylabel("Average Temperature")
plt.title("Climate Change Temperature Trend")
plt.show()