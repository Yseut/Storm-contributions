# Storm-contributions

Yseut Bahuet-Bourret PhD Student (University of the Balearic Islands) y.bahuet@uib.es
Studying the physical processes leading to extreme rainfall changes in Western Mediterrranean, Spanish National Project EPICC

The 'Storm contributions' part of the project aims to understand the types of storm stuctures and mechanisms that lead to Extreme Rainfall Events in the Present Climate in the Region. 

Used data :
List of tracked cyclones in the Mediterranean from 1979 to 2020 (From Flaounas et al 2023 PREPRINT)
ERA5 hourly precipitation data 1979-2020
WRF hourly precipitation data 2011-2020
Tracked convective storms from WRF data 2011-2020

Scripts : 
cyclones_data.py : convert cyclone lists data into panda DataFrame and crop on subdomain too (9 lists for 9 different Confidence Levels (CL))
convective_storms_data.py : create xarrays/(or panda DataFrame?) of convective storms
plot_percentiles_map.py : plot maps of percentiles of hourly PR for WRF and ERA5 data + subplots of seasonal percentiles
plot_density_maps_storms.py : plot density maps of cyclones and convective storms
