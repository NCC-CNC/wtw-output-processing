
# Authors: Marc Edwards
#
# Date: June 29th, 2023
#
# Description: convert the theme rasters into a shapefile of the solution
# planning units with columns as the raster values from each theme. Include all
# PUs, solutions planning units can be extract using the column of 1/0 solution
# values.
#
# Workflow is to convert PUs to points, extract raster values to points, convert
# points to square PU polygons.
#
# Inputs:  1. un-masked solution planning units tif
#          2. un-masked Themes tifs
#
# Outputs: 1. shapefile of solution planning units
#          2. csv table of values that can be joined to PUs
#
#===============================================================================

import arcpy, os
from arcpy.sa import *

arcpy.env.overwriteOutput = True


# path to solutions tif
in_path = "C:/Users/marc.edwards/Downloads/prioritization-2023-06-28/output"
solution = os.path.join(in_path, "s1.tif")

# output path
out_path = "C:/Users/marc.edwards/Downloads/prioritization-2023-06-28"

out_name = "s1_values"

# paths to masked Themes
themes = [os.path.join(in_path, f) for f in os.listdir(in_path) if f.endswith(".tif") and f not in solution]

################################################################################

# make out_path
if not os.path.exists(out_path):
    os.makedirs(out_path)

# make a temp gdb for processing to retain full colnames
arcpy.management.CreateFileGDB(out_path, "output.gdb")
    
# convert PUs to points
arcpy.env.workspace = os.path.join(out_path, "output.gdb")
print("converting to points")
arcpy.conversion.RasterToPoint(solution, "points")

# rename column
new_field = os.path.splitext(os.path.basename(solution))[0]
arcpy.management.AddField("points", new_field, "SHORT")
arcpy.management.CalculateField("points", new_field, "!grid_code!", "PYTHON3")
arcpy.management.DeleteField("points", "grid_code")

# extract raster values to points
print("extracting raster values")
ExtractMultiValuesToPoints("points", themes)

# convert points to polygons
arcpy.analysis.Buffer("points", "buffers", 500)
arcpy.management.FeatureEnvelopeToPolygon("buffers", out_name)

# cleanup
arcpy.management.DeleteField(out_name, ["BUFF_DIST", "ORIG_FID", "pointid"])
arcpy.management.Delete(["points", "buffers"])
