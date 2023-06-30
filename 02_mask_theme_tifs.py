
# Authors: Marc Edwards
#
# Date: June 29th, 2023
#
# Description: mask the provided Themes rasters to the solution raster
#
# Inputs:  1. solution tif
#          2. Themes tifs
#
# Outputs: 1. One masked tif for each input Theme
#
#===============================================================================

import arcpy, os
from arcpy.sa import *

arcpy.env.overwriteOutput = True

# path to solutions tif
in_path = "C:/Users/marc.edwards/Downloads/prioritization-2023-06-28/output"

solution = os.path.join(in_path, "s1.tif")
solution_rast = arcpy.Raster(solution)
solution_rast = SetNull(solution_rast == 0, solution_rast)

# set out folder
out_path = "C:/Users/marc.edwards/Downloads/prioritization-2023-06-28/output_masked"

# make out_path
if not os.path.exists(out_path):
    os.makedirs(out_path)

# get list of Themes to mask, don't include solution
to_mask_list = [os.path.join(in_path, f) for f in os.listdir(in_path) if f.endswith(".tif")]

# loop over Themes, mask to solution, save to out_path
for theme in to_mask_list:
    print(theme)
    out_raster = solution_rast * arcpy.Raster(theme)
    out_raster.save(os.path.join(out_path, os.path.basename(theme)))
