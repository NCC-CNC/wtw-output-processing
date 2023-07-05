# Introduction

This repo holds some useful scripts for processing wheretowork output downloaded from the app.

Typically, users will select one or multiple 'solution' layers to download, and possibly some other Themes, Weights, Includes or Excludes.
The format of the downloads depends on the format of the input data loaded into Where to Work and can be either raster or vector data.

# Raster data

If the input data used raster planning units, downloaded spatial layers from the app are packaged as a single file named `data.tif` which includes all of the requested layers as separate 'bands' in the tif file. The following scripts allow users to extract the 'bands' into both raster and vector formats:

- 01_tif_bands_to_tifs - extracts each 'band' into its own tif file (these should match the input tifs used to create the [four wtw input files](https://github.com/NCC-CNC/wtw-data-prep)).
- 02_mask_theme_tifs - masks the extracted tifs to a requested solution layer.
- 03_tifs_to_featureclass - converts the selected tifs into a geodatabase feature class of planning units where alues in the attribute table represent the values of each layer in each planning unit.

![image](https://github.com/NCC-CNC/wtw-output-processing/assets/10728298/0773c316-0fce-4482-9cc2-81e7ee4735c5)


# Vector

If data was added to Where to Work using planning units in the vector format, then the download will simply be a shapefile of planning units with the requested layers added as columns in the attribute table. Values in the attribute table represent the values of each layer in each planning unit.
