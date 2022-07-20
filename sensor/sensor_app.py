from humidity_info import HumidityData
from statistics import mean
from particle_count_info import ParticleData
from energy_info import EnergyData
##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
##############################
# Module 1 code here:
data = load_sensor_data()
print("Loaded records: {}".format(len(data)))
# Module 2 code here:
house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_data_by_area("id", rec_area=test_area)
print("\nHouse sensor records for area {} = {}".format(test_area, len(recs)))
test_date = datetime.strptime("5/9/20", "%m/%d/%y")
recs = house_info.get_data_by_date("id", rec_date=test_date)
print("House sensor records for date {} = {}".format(test_date.strftime("%m/%d/%y"), len(recs)))
# Module 3 code here:
temperature_data = TemperatureData(data)
recs = temperature_data.get_data_by_area(rec_area=test_area)

print("\tGood Air Quality Recs: {}".format(concentrations["good"]))
print("\tModerate Air Quality Recs: {}".format(concentrations["moderate"]))
print("\tBad Air Quality Recs: {}".format(concentrations["bad"]))
# Module 5 code here: 
# Module 5 code here:
energy_data = EnergyData(data)
recs = energy_data.get_data_by_area(rec_area=test_area)
print("\nHouse Energy sensor records for area {} = {}".format(test_area, len(recs)))
total_energy = energy_data.calculate_energy_usage(data=recs)
print("\tEnergy Usage: {:2.2} Watts".format(total_energy))

recs = energy_data.get_data_by_date(rec_date=test_date)
print("House Energy sensor records for date: {} = {}".format(
    test_date.strftime("%m/%d/%y"), len(recs)))
total_energy = energy_data.calculate_energy_usage(data=recs)
print("\tEnergy Usage: {:2.2} Watts".format(total_energy)) 