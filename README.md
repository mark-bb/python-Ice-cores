# Paleo-climate ice corn research with a python program  

Comma-separated values (CSV) files in the data/data.zip file are used by the Ice_cores.py python program for the research.  
All the charts described below are printed on the same figure. 

The program consists of a number of functions:  
* part1: reads the CSV file data/edc-co2-2008-bern-noaa.txt passed as a parameter and Builds a corn CO2 dependency on age chart (1-st line)
* part2_1: reads the CSV file data/gripd18o.txt and builds a corn d18o dependency on age chart (2-nd line, left)
* part2_2: reads the CSV file data/gripd18o.txt and builds a Temperature dependency on age chart (2-nd line, right)
* part3_1: reads the CSV file data/edc3deuttemp2007.txt and builds a temperature dependency on age chart (3-rd line, left)
* part3_2: reads the CSV files data/edc-co2-2008-bern-noaa.txt & data/edc3deuttemp2007.txt and builds a CO2 & temperature dependency on age chart (3-rd line, right)
* part4_1: reads the CSV file data/Elbrus_raw_data.txt and builds a Nh4 dependency on depth chart (4-th line, left)
* part4_2: reads the CSV file data/Elbrus_annual_summer.txt and auilds a Nh4, No3, So4 dependency on year chart (4-th line, right)

