simulation_settings:

# Choose how to define simulation duration:
# Options: "date_range", "seasonal", "full_year"
simulation_mode: "seasonal"

# Used only if simulation_mode is "date_range"
date_start: "2020-07-01"
date_end: "2020-07-02"
  
  #Calibration factor
  peak_enlarge: 0.15

  # The folder where the simulation results will be saved.
  # Example: "output" will save the results in a folder named "output".
  output_folder: 'output' 
  
  parallel: false

  # The number of days for each season in the simulation. You can specify different values for each season.
  days_per_season:
    summer: 90  # Specify number of days for the summer season
    winter: 2  # Specify number of days for the winter season
    spring: 90   # Specify number of days for the spring season
    autumn: 90  # Specify number of days for the autumn season
    

  regions:
    - BOLL
    - BOV
    - BOHL
    - MOZN
    - KNYC

  # A list of seasons to simulate. You can add more seasons (e.g., spring, summer) or modify them.
  # Example: ["summer", "winter", "spring", "autumn"] defines four seasons.
  seasons:
    - summer
    - winter
    - spring
    - fall
   
  # Simulation levels determine at which level the simulation will run. 
  # Options: "energy_service" (individual services like lighting, refrigeration),
  # "user_type" (low_consumption, high_consumption users), 
  # "sector" (households, community services, income-generating activities),
  # "community" (full community simulation including all sectors).
  simulation_levels:
    - energy_services
    - sector
    - user_type
    - community

  sectors:  # The sectors involved in the simulation. Each sector contains different user types and their energy services.
    households:
        sufficiency:   # Household sector: Contains different user types based on consumption level.
          count: 3   # 'count' defines how many high-consumption households to simulate.
          energy_service:  ["illumination", 'cold_storage']  # 'energy_service' lists the energy services available for this user type.
                              # Example: ["illumination", "refrigeration", "ict"] for high consumption households.
              #- illumination
              #- ICT
              #- cold_storage
              #- space_cooling
              #- space_heating
              #- water_heating
        
    community_services:   # Community services sector: Includes community services like schools, health posts, etc.    
         medium_school:
         count: 0
            energy_service:
                - illumination
                - ICT
                - cold_storage
                - space_cooling
                - space_heating
                - water_heating
                
        health_post:
        count: 0
            energy_service: 
                - illumination
                - ICT
                - cold_storage
                - space_cooling
                - space_heating
                - water_heating
                - medical_equip
       
    income_generating_activity:    # Income generating activities sector: Includes stores, workshops, etc.
        workshop:
        count: 0
            energy_service:
                - illumination
                - ICT
                - welding
                - grinding
                - sawing
                - cold_storage
                - space_cooling
                - space_heating
                - water_heating
        grocery_store:
        count: 0
            energy_service:
                - illumination
                - ICT
                - cold_storage
                - space_cooling
                - space_heating
                - water_heating
        entertainment:
        count: 0
                - ICT
                - cold_storage
                - illumination
        restaurant:
        count: 0
            - illumination
            - food_processing
            - cold_storage
        quinoa_processing:
        count: 0
            - washing
            - milling
        mill:
        count: 0
            - milling
        carpentry:
        count: 0
            - illumination
            - special_equipment
            - space_cooling
        
        copy_center:
        count: 0
            - illumination
            - cold_storage
            - ICT
            - special_equipment
        
        milk_production:
        count: 0
            - illumination
            - cold_storage
            - special_equipment
        
        flour_production:
        count: 0
            - drying
            - milling
            - toasting
            - water_pumping
        
            
        
        