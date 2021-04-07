import pandas as pd
import numpy as np

df = pd.read_csv ('12_2_20-3_27_21 - results-20210328-110018.csv')

# Run print statement to ensure the data has been read in correctly 
# print (df)

# -----------------------------------------------------------
# VARIABLES IN FRAME 
# trend - -1 (improving), 0 (constant), 1 getting worse 
# street 
# endnode - nearest street to jam end 
# nimages - images related to jame taken 
# speed - traffic speed in irregularity 
# id - irregularity identifier 
# severity - calculated severity of irregularity compared to historical speed (5 most severe)
# type 
# highway - boolean 
# seconds - historical time to travel the jam length minus the free flow time
# detectionDateTS - type timestamp 
# driversCount - 
# geo - geography of the jam 
# geoWKT - geography of the jam 
# startNode - nearest street to jame start 
# updateDateTS - Last update 
# regularSpeed - historical regular speed in kmh (convert to mph)
# length - irregularity length 
# delaySeconds - delay in seconds from regular speed 
# jamLevel - traffic congestion (0 = free flow, 5 = blocked )
# causeType
# causeAlertUUID - alert ID 
# -----------------------------------------------------------

#print(df.head())
#print(df.columns)

# Santa's Little Helpers 
# Convert to KPH -> MPH 
def toMPH(x):
    return x/1.609

df['regularSpeed'] = df['regularSpeed'].apply(toMPH)
df = df.sort_values(by="detectionDateTS")
print(df)