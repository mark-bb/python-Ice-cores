import numpy as np
import matplotlib.pyplot as plt

def part1(ax, ax_idx1, ax_idx2, file_name):
    '''
    Part 1: Builds a corn CO2 dependency on age chart
    Parameters:
    - ax: subplot object created outside
    - ax_idx1: 1-st index of the chart in the figure
    - ax_idx2: 2-nd index of the chart in the figure
    - file_name: input data set file name
    '''
    
    # Skipping first 278 lines of file - comments and column header
    # Using only 2 columns (with 0-based indexes 1 and 2) out of 4 columns
    x, y = np.loadtxt(file_name, unpack='true', skiprows=278, usecols=(1,2))

    plt = ax[ax_idx1, ax_idx2]
    plt.plot(x, y)
    plt.set_xlabel('Возраст', fontsize=8) # x axis label
    plt.set_ylabel('CO2', fontsize=8) # y axis lable
    plt.set_title('Часть1: График CO2 в зависимости от возраста', fontsize=8) # chart title


def part2_1(ax, ax_idx1, ax_idx2, file_name, age_min=10000, age_max=50000):
    '''
    Part 1: Builds a corn d18o dependency on age chart
    Parameters:
    - ax: subplot object created outside
    - ax_idx1: 1-st index of the chart in the figure
    - ax_idx2: 2-nd index of the chart in the figure
    - file_name: input data set file name
    - age_min: minimum age for mask (10000 if not specified)
    - age_max: maximum age for mask (50000 if not specified)
    '''
    
    # Skipping first 37 lines of file - comments and column header
    # Using only 2 columns (with 0-based indexes 1 and 2) out of 3 columns
    y, x = np.loadtxt(file_name, unpack='true', skiprows=37, usecols=(1,2))

    mask_age = (age_min <= x) & (x <= age_max) # age mask
    plt = ax[ax_idx1, ax_idx2]
    plt.plot(x[mask_age], y[mask_age])
    plt.set_xlabel('Возраст', fontsize=8) # x axis label
    plt.set_ylabel('d18o', fontsize=8) # y axis lable
    plt.set_title('Часть2: График d18o в зависимости от возраста', fontsize=8) # chart title

def part2_2(ax, ax_idx1, ax_idx2, file_name, age_min=10000, age_max=50000):
    '''
    Part 1: Builds Temperature dependency on age chart
    Parameters:
    - ax: subplot object created outside
    - ax_idx1: 1-st index of the chart in the figure
    - ax_idx2: 2-nd index of the chart in the figure
    - file_name: input data set file name
    - age_min: minimum age for mask (10000 if not specified)
    - age_max: maximum age for mask (50000 if not specified)
    '''
    
    # Skipping first 37 lines of file - comments and column header
    # Using only 2 columns (with 0-based indexes 1 and 2) out of 3 columns
    y, x = np.loadtxt(file_name, unpack='true', skiprows=37, usecols=(1,2))
    y = (13.7 + y)/0.67

    mask_age = (age_min <=x) & (x <= age_max) # age mask

    plt = ax[ax_idx1, ax_idx2]
    plt.plot(x[mask_age], y[mask_age])
    plt.set_xlabel('Возраст', fontsize=8) # x axis label
    plt.set_ylabel('Температура', fontsize=8) # y axis lable
    plt.set_title('Часть2: График температуры в зависимости от возраста', fontsize=8) # chart title

def part3_1(ax, ax_idx1, ax_idx2, file_name):
    '''
    Part 3: Builds a temperature dependency on age chart
    Parameters:
    - ax: subplot object created outside
    - ax_idx1: 1-st index of the chart in the figure
    - ax_idx2: 2-nd index of the chart in the figure
    - file_name: input data set file name
    '''

    # Skipping first 104 lines of file - comments and column header
    # Using only 2 columns (with 0-based indexes 2 and 4) out of 5 columns
    x3, y3 = np.loadtxt(file_name, unpack='true', skiprows=104, usecols=(2,4), comments='#')
    plt = ax[ax_idx1, ax_idx2]
    plt.plot(x3, y3)
    plt.set_xlabel('Возраст', fontsize=8) # x axis label
    plt.set_ylabel('Температура', fontsize=8) # y axis lable
    title = 'Часть3: График температуры в зависимости от возраста'
    plt.set_title(title, fontsize=8) # chart title

def part3_2(ax, ax_idx1, ax_idx2, file_name1, file_name3, age_min=600000, age_max=800000):
    '''
    Part 3: Builds a CO2 & temperature dependency on age chart
    Parameters:
    - ax: subplot object created outside
    - ax_idx1: 1-st index of the chart in the figure
    - ax_idx2: 2-nd index of the chart in the figure
    - file_name1: input data set file name from Part 1
    - file_name3: input data set file name from Part 3
    - age_min: minimum age for mask (600000 if not specified)
    - age_max: maximum age for mask (800000 if not specified)
    '''

    x1, y1 = np.loadtxt(file_name1, unpack='true', skiprows=278, usecols=(1,2))
    x3, y3 = np.loadtxt(file_name3, unpack='true', skiprows=104, usecols=(2,4), comments='#')
    mask1_age = (age_min <= x1) & (x1 <= age_max) # age mask
    mask3_age = (age_min <= x3) & (x3 <= age_max) # age mask
    plt = ax[ax_idx1, ax_idx2]
    plt.plot(x1[mask1_age], y1[mask1_age])
    plt.plot(x3[mask3_age], y3[mask3_age])
    plt.set_xlabel('Возраст', fontsize=8) # x axis label
    plt.set_ylabel('CO2 / Температура', fontsize=8) # y axis lable
    title = 'Часть3: График CO2 и температуры в зависимости от возраста'
    plt.set_title(title, fontsize=8) # chart title
    plt.legend(['CO2', 'Отклонение температуры'], fontsize=8) # подпись легенды к каждому графику

def part4_1(ax, ax_idx1, ax_idx2, file_name, depth_min=None, depth_max=None):
    '''
    Part 4: Builds a Nh4 dependency on depth chart
    Parameters:
    - ax: subplot object created outside
    - ax_idx1: 1-st index of the chart in the figure
    - ax_idx2: 2-nd index of the chart in the figure
    - file_name: input data set file name
    - depth_min: minimum depth for mask (mask is not used if not specified)
    - depth_max: maximum depth for mask (mask is not used if not specified)
    '''
    x, y = np.loadtxt(file_name, unpack='true', usecols=(0,4), comments='#')
    plt = ax[ax_idx1, ax_idx2]
    if (depth_min is not None) & (depth_max is not None):
        # Use mask if min & max are spesified
        mask_depth = (depth_min <= x) & (x <= depth_max) # debth mask if passed
        plt.plot(x[mask_depth], y[mask_depth])
    else:
        plt.plot(x, y)
    plt.set_xlabel('Глубина', fontsize=8) # x axis label
    plt.set_ylabel('Nh4', fontsize=8) # y axis lable
    title = 'Часть4: График Nh4 в зависимости от глубины'
    plt.set_title(title, fontsize=8) # chart title

def part4_2(ax, ax_idx1, ax_idx2, file_name):
    '''
    Part 4: Builds a Nh4, No3, So4 dependency on year chart
    Parameters:
    - ax: subplot object created outside
    - ax_idx1: 1-st index of the chart in the figure
    - ax_idx2: 2-nd index of the chart in the figure
    - file_name: input data set file name
    '''
    x, y_Nh4, y_No3, y_So4 = np.loadtxt(file_name, unpack='true', comments='#')
    plt = ax[ax_idx1, ax_idx2]
    plt.plot(x, y_Nh4)
    plt.plot(x, y_No3)
    plt.plot(x, y_So4)
    plt.set_xlabel('Год', fontsize=8) # x axis label
    plt.set_ylabel('ppb', fontsize=8) # y axis label
    title = 'Часть4: График Nh4, No3, So4 в зависимости от года'
    plt.set_title(title, fontsize=8) # chart title
    plt.legend(['Nh4', 'No3', 'So4'], fontsize=8) # подпись легенды к каждому графику


#
# Main
#

fig, ax = plt.subplots(4, 2, figsize=(20, 10))

# File names
file_name1='data/edc-co2-2008-bern-noaa.txt'
file_name2='data/gripd18o.txt'
file_name3='data/edc3deuttemp2007.txt'
file_name4_1='data/Elbrus_raw_data.txt'
file_name4_2='data/Elbrus_annual_summer.txt'

# Placing all charts on the subplot
part1(ax=ax, ax_idx1=0, ax_idx2=0, file_name=file_name1)
#It's possible to filter ages if needed
#part2_1(ax=ax, ax_idx1=1, ax_idx2=0, file_name=file_name2, age_min=10000, age_max=11000)
#part2_2(ax=ax, ax_idx1=1, ax_idx2=1, file_name=file_name2, age_min=10000, age_max=11000)
part2_1(ax=ax, ax_idx1=1, ax_idx2=0, file_name=file_name2)
part2_2(ax=ax, ax_idx1=1, ax_idx2=1, file_name=file_name2)
part3_1(ax=ax, ax_idx1=2, ax_idx2=0, file_name=file_name3)
part3_2(ax=ax, ax_idx1=2, ax_idx2=1, file_name1=file_name1, file_name3=file_name3)
part4_1(ax=ax, ax_idx1=3, ax_idx2=0, file_name=file_name4_1)
#It's possible to filter depth if needed
#part4_1(ax=ax, ax_idx1=3, ax_idx2=0, file_name=file_name4_1, depth_min=35.6, depth_max=36)
part4_2(ax=ax, ax_idx1=3, ax_idx2=1, file_name=file_name4_2)

plt.tight_layout()
plt.show()
