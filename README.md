# STB0100 - NASA SPACE APPS CHALLENGE 2021 BRESCIA

Challenge: <b>"Identifying risk with science + communities"</b>

Project: <b>"Predicting landslides with AI"</b>

Authors:
<li>Abdelghani Msaad</li>
<li>Alessandro Crispiels</li>
<li>Gabriele Ceresara</li>

----

## Overview of the project

Our team developed a concept for a machine learning model, which uses a combination of satellite data and deep neural network to define a risk factor for possible landslides.<br/>
This risk factor is then shown on a simple site, which shows the current prediction of risk factors on a global map, showing the zones with high risk factors through an overlay.<br/>
This service allows everyone who has access to the internet to discover if a zone has become dangerous and could be hit by a landslide.

## Files present in the repository

<b>N.B.</b> As this project requires a lot of time, both for the data collection and processing and for the whole infrastructure surrounding the model, this repository hosts 
only a few scripts actually completed, which will be useful for a future complete developement, while most of the main script is only a structure of the whole concept, containing informations on each passage of the project and a few guidelines for the actual creation of the code.
<br/><br/>
<li>"res": folder containing data for both the terrain temperature and vegetation distribution as compressed .csv files.
<li>"3_STB_ImagePocessing.py": python script used to open .tif images and convert them in .csv files through numpy's array.
<li>"ALPSMLC30_N032E077_DSM.tif": example of an altitude map obtained from the "ALOS World 3D - 30m" database containing the map of the region between 32° and 33° N and 77° and 78° E.
<li>"IDENTIFYING_RISK_WITH_SCIENCE.pptx": powerpoint file used for the presentation of the project to the local judges.
<li><b>"NSAC_ML.ipynb"</b>: main notebook script containing the structure of the data processing and the neural network design, also contains a few details about possible future developements and applications.
<li>"README.md": this file.
<li>"from_tif_to_csv.py": updated version of 3_STB_ImagePocessing.py, which allows for the conversion of multiple files in a single run.
<li>"nasa_global_landslide_catalog_point.csv": dataset containing a list of landslides collected by the Cooperative Open Online Landslide Repository (COOLR).
