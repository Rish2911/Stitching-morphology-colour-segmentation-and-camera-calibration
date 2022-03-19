1) Copy and paste all the files in the folder code (including input_output folders) and make that folder your working directory.

Image for K mean custering:   ![alt text](https://github.com/Rish2911/Stitching-morphology-colour-segmentation-and-camera-calibration/blob/main/coloursegmentation_input_output/Q4image.png) <br />
Image for Morphology:
![alt text](https://github.com/Rish2911/Stitching-morphology-colour-segmentation-and-camera-calibration/blob/main/morphology_input_output/Q1image.png)<br />
Image for Stitching left: 
![alt text](https://github.com/Rish2911/Stitching-morphology-colour-segmentation-and-camera-calibration/blob/main/stitching_input_output/left.png)<br />
Image for Stitching right:
![alt text](https://github.com/Rish2911/Stitching-morphology-colour-segmentation-and-camera-calibration/blob/main/stitching_input_output/right.png) <br />

2) For running all the codes you need to create an environment first and then install the libraries.
Note: for running the code of image sticthing which is image_sticthing.py, you need to create a custom environment with opencv 3.4.2. in order to use SIFT. 
3) Install required packages onto your virtual environment. Replace “myenv”with your environment name. 
  Enter the following commands in your terminal window. Press ‘y’ when prompted. 
  a. conda create -n myenv python=3.7
  b. conda activate myenv
  c. conda install -c conda-forge opencv=4.1.0
  d. conda install -c anaconda numpy
  e. conda install -c conda-forge matplotlib
  f. conda install -c conda-forge imutils
  g. (optional) conda install spyder=4.2.0
  h. (optional) spyder
  i. pip3 install sympy 



4) How to run the codes:
    a) After installing all the libraries, we are ready to run the codes. Codes are python script

    b) Problem  codes are in the file named 'morphology.py' for question 1, 'image_stitching.py' for question 2, 'camera_calibration.py' for question 3 and 'colour_segmentation.py' for question 4. Open the file, load your environment.


    Sample Commands : python3 morphology.py
    
    Please go through the project report named as rsingh24.pdf for more details.


    Please contact me for any problem, at rsingh24@umd.edu
    
5) Output:
Image for K mean custering:   ![alt text](https://github.com/Rish2911/Stitching-morphology-colour-segmentation-and-camera-calibration/blob/main/coloursegmentation_input_output/clustered_image.png) <br />
Image for Morphology:
![alt text](https://github.com/Rish2911/Stitching-morphology-colour-segmentation-and-camera-calibration/blob/main/morphology_input_output/opened_image.png)<br />
Stitched Image: 
![alt text](https://github.com/Rish2911/Stitching-morphology-colour-segmentation-and-camera-calibration/blob/main/stitching_input_output/output.png)<br />

