#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:16:28 2024

@author: claudia
"""

import pandas as pd

from ramp.core.core import User
User_list = []

#Defining users
H = User("household", 1)
User_list.append(H)

H_shower_P = pd.read_csv('shower_P_LL.csv')

'''
ES SCENARIO
'''
#Summer

#Illumination
H_indoor_bulb = H.Appliance(4,7,2,360,0.2,10)
H_indoor_bulb.windows([300,420],[1020,1440],0.35)
         
H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

#thermal comfort
H_Fan = H.Appliance(4,30,2,480,0.27,30)
H_Fan.windows([480,1200],[0,0],0.35)

#Nutrition

H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 3)
H_Freezer.windows([0, 1440], [0, 0])
H_Freezer.specific_cycle_1(200, 20, 5, 10) #intensivo
H_Freezer.specific_cycle_2(200, 15, 5, 15) #intemedio
H_Freezer.specific_cycle_3(200, 10, 5, 20) #standard
H_Freezer.cycle_behaviour([480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440])

#Water heating
#It is assumed is performed using GLP

#ICT
H_TV = H.Appliance(1,30,2,120,0.1,5)
H_TV.windows([1080,1440],[0,60],0.35)

H_Radio = H.Appliance(1,36,2,120,0.1,5)
H_Radio.windows([390,450],[1082,1260],0.35)

H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
H_Phone_charger.windows([1020,1440],[0,300],0.35)

H_Laptop = H.Appliance(1,70,1,90,0.3,30)
H_Laptop.windows([960,1200],[0,0],0.35)

#Fall

#Shelter and living conditions
#ilumination
H_indoor_bulb = H.Appliance(4,7,3,360,0.2,10)
H_indoor_bulb.windows([360,420],[1020,1440],0.35,[0,60])
         
H_outdoor_bulb = H.Appliance(2,14,1,240,0.2,10)
H_outdoor_bulb.windows([1020,1380],[0,0],0.35)

#thermal comfort
H_Fan = H.Appliance(1,30,2,400,0.27,30)
H_Fan.windows([600,1200],[0,0],0.35)

#Nutrition

H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 3)
H_Freezer.windows([0, 1440], [0, 0])
H_Freezer.specific_cycle_1(200, 20, 5, 10) #intensivo
H_Freezer.specific_cycle_2(200, 15, 5, 15) #intemedio
H_Freezer.specific_cycle_3(200, 10, 5, 20) #standard
H_Freezer.cycle_behaviour([480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440])


#Hygiene
#Water heating
#It is assumed is performed using GLP

#ICT
H_TV = H.Appliance(1,30,2,120,0.1,5)
H_TV.windows([1080,1440],[0,60],0.35)

H_Radio = H.Appliance(1,36,2,120,0.1,5)
H_Radio.windows([390,450],[1082,1260],0.35)

H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
H_Phone_charger.windows([1020,1440],[0,300],0.35)

H_Laptop = H.Appliance(1,70,1,90,0.3,30)
H_Laptop.windows([960,1200],[0,0],0.35)

#Winter
#Shelter and living conditions
#ilumination

H_indoor_bulb = H.Appliance(4,7,3,360,0.2,10)
H_indoor_bulb.windows([360,420],[1020,1440],0.35,[0,60])
         
H_outdoor_bulb = H.Appliance(2,14,1,240,0.2,10)
H_outdoor_bulb.windows([1020,1380],[0,0],0.35)

#thermal comfort
#Not used during winter

#Nutrition
H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2) #Two cycles for cold season in ll
H_Freezer.windows([0, 1440], [0, 0])
H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
H_Freezer.cycle_behaviour([300, 1200], [0, 0], [0, 299], [1201, 1440])

#Hygiene
#Water heating
#It is assumed is performed using GLP

#ICT
H_TV = H.Appliance(1,30,2,120,0.1,5)
H_TV.windows([1080,1440],[0,60],0.35)

H_Radio = H.Appliance(1,36,2,120,0.1,5)
H_Radio.windows([390,450],[1082,1260],0.35)

H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
H_Phone_charger.windows([1020,1440],[0,300],0.35)

H_Laptop = H.Appliance(1,70,1,90,0.3,30)
H_Laptop.windows([960,1200],[0,0],0.35)

#Spring

#Shelter and living conditions
#ilumination

H_indoor_bulb = H.Appliance(4,7,2,360,0.2,10)
H_indoor_bulb.windows([300,420],[1020,1440],0.35)
         
H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

#thermal comfort
H_Fan = H.Appliance(4,30,2,540,0.27,30)
H_Fan.windows([540,1200],[0,0],0.35)

#Nutrition

H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 3)
H_Freezer.windows([0, 1440], [0, 0])
H_Freezer.specific_cycle_1(200, 20, 5, 10) #intensivo
H_Freezer.specific_cycle_2(200, 15, 5, 15) #intemedio
H_Freezer.specific_cycle_3(200, 10, 5, 20) #standard
H_Freezer.cycle_behaviour([480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440])

#H_Blender = H.Appliance(1, 50, 3, 30, 0.1, 1, occasional_use=0.33)
#H_Blender.windows([420, 480], [660, 750], 0.35, [1140, 1200])

#Hygiene
#Water heating
#It is assumed is performed using GLP

#ICT
H_TV = H.Appliance(1,30,2,120,0.1,5)
H_TV.windows([1080,1440],[0,60],0.35)

H_Radio = H.Appliance(1,36,2,120,0.1,5)
H_Radio.windows([390,450],[1082,1260],0.35)

H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
H_Phone_charger.windows([1020,1440],[0,300],0.35)

H_Laptop = H.Appliance(1,70,1,90,0.3,30)
H_Laptop.windows([960,1200],[0,0],0.35)

'''
TRADITIONAL APPLIANCES
'''
#Summer

# #Illumination
# H_indoor_bulb = H.Appliance(4,25,2,360,0.2,10)
# H_indoor_bulb.windows([300,420],[1020,1440],0.35)
         
# H_outdoor_bulb = H.Appliance(2,40,1,180,0.2,10)
# H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

# #thermal comfort
# H_Fan = H.Appliance(4,30,2,480,0.27,30)
# H_Fan.windows([480,1200],[0,0],0.35)

# #Nutrition

# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 3)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 20, 5, 10) #intensivo
# H_Freezer.specific_cycle_2(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_3(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour([480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440])

# #Water heating
# #It is assumed is performed using GLP

# #ICT
# H_TV = H.Appliance(1,150,2,120,0.1,5)
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,150,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

#Fall

#Shelter and living conditions
#ilumination
# H_indoor_bulb = H.Appliance(4,25,3,360,0.2,10)
# H_indoor_bulb.windows([360,420],[1020,1440],0.35,[0,60])
         
# H_outdoor_bulb = H.Appliance(2,40,1,240,0.2,10)
# H_outdoor_bulb.windows([1020,1380],[0,0],0.35)

# #thermal comfort
# H_Fan = H.Appliance(1,30,2,400,0.27,30)
# H_Fan.windows([600,1200],[0,0],0.35)

# #Nutrition

# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 3)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 20, 5, 10) #intensivo
# H_Freezer.specific_cycle_2(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_3(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour([480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440])


# #Hygiene
# #Water heating
# #It is assumed is performed using GLP

# #ICT
# H_TV = H.Appliance(1,150,2,120,0.1,5)
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,150,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

#Winter
#Shelter and living conditions
#ilumination

# H_indoor_bulb = H.Appliance(4,25,3,360,0.2,10)
# H_indoor_bulb.windows([360,420],[1020,1440],0.35,[0,60])
         
# H_outdoor_bulb = H.Appliance(2,40,1,240,0.2,10)
# H_outdoor_bulb.windows([1020,1380],[0,0],0.35)

# #thermal comfort
# #Not used during winter

# #Nutrition
# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2) #Two cycles for cold season in ll
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour(
#     [480, 1200], [0, 0], [0, 299], [1201, 1440])

# #Hygiene
# #Water heating
# #It is assumed is performed using GLP

# #ICT
# H_TV = H.Appliance(1,150,2,120,0.1,5)
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,150,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

#Spring

#Shelter and living conditions
#ilumination

# H_indoor_bulb = H.Appliance(4,25,2,360,0.2,10)
# H_indoor_bulb.windows([300,420],[1020,1440],0.35)
         
# H_outdoor_bulb = H.Appliance(2,40,1,180,0.2,10)
# H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

# #thermal comfort
# H_Fan = H.Appliance(4,30,2,540,0.27,30)
# H_Fan.windows([540,1200],[0,0],0.35)

# #Nutrition

# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 3)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 20, 5, 10) #intensivo
# H_Freezer.specific_cycle_2(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_3(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour([480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440])

# #H_Blender = H.Appliance(1, 50, 3, 30, 0.1, 1, occasional_use=0.33)
# #H_Blender.windows([420, 480], [660, 750], 0.35, [1140, 1200])

# #Hygiene
# #Water heating
# #It is assumed is performed using GLP

# #ICT
# H_TV = H.Appliance(1,150,2,120,0.1,5)
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,150,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

'''
MODERN APPLIANCES
'''
# #Summer

#Illumination
# H_indoor_bulb = H.Appliance(4,7,2,360,0.2,10)
# H_indoor_bulb.windows([300,420],[1020,1440],0.35)
         
# H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
# H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

# #thermal comfort
# H_Air_Conditioner = H.Appliance(1,900,2,400,0.2,15)
# H_Air_Conditioner.windows([480,1200],[0,0],0.35)

# #Nutrition

# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 3)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 20, 5, 10) #intensivo
# H_Freezer.specific_cycle_2(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_3(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour([480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440])

# #Water heating
# H_shower = H.Appliance(1,5500,2,40,0.1,3, thermal_P_var = 0.1)
# H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands

# #ICT
# H_TV = H.Appliance(1,30,2,120,0.1,5)
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,70,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

#Fall

#Shelter and living conditions
#ilumination
# H_indoor_bulb = H.Appliance(4,7,3,360,0.2,10)
# H_indoor_bulb.windows([360,420],[1020,1440],0.35,[0,60])
         
# H_outdoor_bulb = H.Appliance(2,14,1,240,0.2,10)
# H_outdoor_bulb.windows([1020,1380],[0,0],0.35)

# #thermal comfort
# H_Air_Conditioner = H.Appliance(1,900,2,300,0.2,15)
# H_Air_Conditioner.windows([600,1200],[0,0],0.35)

# #Nutrition

# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 3)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 20, 5, 10) #intensivo
# H_Freezer.specific_cycle_2(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_3(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour([480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440])


# #Hygiene
# #Water heating
# H_shower = H.Appliance(1,5500,2,40,0.1,3, thermal_P_var = 0.2)
# H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands

# #ICT
# H_TV = H.Appliance(1,30,2,120,0.1,5)
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,70,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

#Winter
#Shelter and living conditions
#ilumination

# H_indoor_bulb = H.Appliance(4,7,3,360,0.2,10)
# H_indoor_bulb.windows([360,420],[1020,1440],0.35,[0,60])
         
# H_outdoor_bulb = H.Appliance(2,40,1,240,0.2,10)
# H_outdoor_bulb.windows([1020,1380],[0,0],0.35)

# #thermal comfort
# #Not used during winter

# #Nutrition
# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 2) #Two cycles for cold season in ll
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_2(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour(
#     [480, 1200], [0, 0], [0, 299], [1201, 1440])

# #Hygiene
# #Water heating
# H_shower = H.Appliance(1,5500,2,40,0.2,3, thermal_P_var = 0.3)
# H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands

# #ICT
# H_TV = H.Appliance(1,30,2,120,0.1,5)
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,70,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

# #Spring

#Shelter and living conditions
#ilumination

# H_indoor_bulb = H.Appliance(4,7,2,360,0.2,10)
# H_indoor_bulb.windows([300,420],[1020,1440],0.35)
         
# H_outdoor_bulb = H.Appliance(2,14,1,180,0.2,10)
# H_outdoor_bulb.windows([1140,1380],[0,0],0.35)

# #thermal comfort
# H_Air_Conditioner = H.Appliance(1,900,2,450,0.2,15)
# H_Air_Conditioner.windows([480,1200],[0,0],0.35)

# #Nutrition

# H_Freezer = H.Appliance(1, 200, 1, 1440, 0, 30, "yes", 3)
# H_Freezer.windows([0, 1440], [0, 0])
# H_Freezer.specific_cycle_1(200, 20, 5, 10) #intensivo
# H_Freezer.specific_cycle_2(200, 15, 5, 15) #intemedio
# H_Freezer.specific_cycle_3(200, 10, 5, 20) #standard
# H_Freezer.cycle_behaviour([480, 1200], [0, 0], [300, 479], [0, 0], [0, 299], [1201, 1440])


# #Hygiene
# #Water heating
H_shower = H.Appliance(1,5500,2,40,0.1,3, thermal_P_var = 0.1)
H_shower.windows([360,540],[1080,1260],0.2) #Use thermal series from lowlands

# #ICT
# H_TV = H.Appliance(1,60,2,120,0.1,5)
# H_TV.windows([1080,1440],[0,60],0.35)

# H_Radio = H.Appliance(1,36,2,120,0.1,5)
# H_Radio.windows([390,450],[1082,1260],0.35)

# H_Phone_charger = H.Appliance(4,5,2,120,0.2,10)
# H_Phone_charger.windows([1020,1440],[0,300],0.35)

# H_Laptop = H.Appliance(1,70,1,90,0.3,30)
# H_Laptop.windows([960,1200],[0,0],0.35)

if __name__ == "__main__":
    from ramp.core.core import UseCase

    uc = UseCase(
        users=User_list,
        parallel_processing=False,
        #date_start="2022-01-01", date_end="2022-03-31" #SUMMER
        #date_start="2022-04-01", date_end="2022-06-30"  #FALL
        #date_start="2022-07-01", date_end="2022-09-30"  #WINTER
        date_start="2022-10-01", date_end="2022-12-31"  #SPRING
        )
    uc.initialize(peak_enlarge=0.15)

    Profiles_list = uc.generate_daily_load_profiles(flat=False)

    # post-processing
    from ramp.post_process import post_process as pp

    Profiles_avg, Profiles_list_kW, Profiles_series = pp.Profile_formatting(
        Profiles_list
    )
    pp.Profile_series_plot(
        Profiles_series
    )  # by default, profiles are plotted as a series
    
    if (
        len(Profiles_list) > 1
    ):  # if more than one daily profile is generated, also cloud plots are shown
        pp.Profile_cloud_plot(Profiles_list, Profiles_avg)
        
    # this would be a new method using work of @mohammadamint
    pp.export_series(Profiles_series, j=None, fname= None, ofname= 'shower_spring_LL.csv')