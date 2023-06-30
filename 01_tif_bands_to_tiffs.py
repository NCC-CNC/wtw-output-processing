#
# Authors: Marc Edwards
#
# Date: June 28th, 2023
#
# Description: separates the wtw download data.tif into multiple files 
#
# Inputs:  1. data.tif
#
# Outputs: 1. One tif for each band in data.tif
#
#===============================================================================

import arcpy, os

in_file = "C:/Users/marc.edwards/Downloads/prioritization-2023-06-28/data.tif"

out_path = "C:/Users/marc.edwards/Downloads/prioritization-2023-06-28/output"


################################################################################

# load raster
rast = arcpy.Raster(in_file)

# count bands
n_bands = rast.getRasterInfo().getBandCount()

# make out_path
if not os.path.exists(out_path):
    os.makedirs(out_path)

# loop over bands and save
for i in range(1, n_bands + 1):

    print(i)

    # get raster name
    out_name = os.path.basename(str(rast.getRasterBands(i)))
    
    # save
    rast.getRasterBands(i).save(os.path.join(out_path ,str(out_name) + ".tif"))
