.. _dgsplanner:

=============================
DGSPlanner Tutorial and Guide
=============================

.. contents::
  :local:

Introduction and Overview
+++++++++++++++++++++++++
DGSPlanner is a tool used to generate regions of measurement coverage 
in energy transfer and reciprocal space as a function of crystal geometry
and ranges of sample rotation. 

This document describes how to use the DGSPlanner to set up single crystal 
inelastic measurements for a direct geometry spectrometer (DGS).  
The document first goes through a step-by-step tutorial .  
After the tutorial, the document presents the current DGSPlanner 
documentation available directly from the application.

Tutorial
++++++++
    
1. Prerequisites
----------------

If you don’t have the latest version of Mantid installed on your local computer, you can use the remote analysis.sns.gov machines.
To log in, use one of the following options:

  * From the analysis machines available at the instrument cabin, one can use xcams or ucams userID and password to login.
  * In a web browser, navigate to https://analysis.sns.gov to use xcams or ucams userID and password to login.
  * If you do not have an xcams account, please navigate to https://user.ornl.gov/Account/Login and use the Register link to create an account. 
  


2. Start DGSPlanner
-------------------

There are two options to start the interface:

  * Start DGSPlanner from Mantid Workbench. Type `mantidworkbenchnighlty` at the command line prompt and press the Enter key.  Once Mantid Workbench loads navigate to `Interfaces` -> `Direct` -> `DGSPlanner`.
  * Start DGSPlanner from the command line. At the command line type

    python3 /opt/mantidnightly/scripts/DGSPlanner.py


3. DGSPlanner window
--------------------

.. plot_gui:: dgs_picture generate_picture dgs_planner_main.png
   :name: dgs-fig1
   :align: center

   DgsPlanner interface

The main interface is shown in :numref:`dgs-fig1`.  Input parameters are on the left side of the window and the calculated detector coverage appears in the right portion of the window.

The image in the middle of the window shows the definition of the three rotation axes in relation to the incident beam and the sample.  This image can be clicked on and rotated.  Nearly all DGS measurements will only use the psi rotation angle. 


4. Parameters 
-------------

Enter the information for the calculation on the left side of the window.  Work from the top of the window down toward the bottom of the window.
  a. **Instrument** – Use the Instrument pull down menu to choose the instrument that is being used.
  b. **Incident Energy** – Enter the incident energy for the calculation in units of meV.
  c. **S2** (only if the instrument selected is HYSPEC) - the angle of the detector tank
  d. **Fast option** – check the fast option to only use 25% of detector pixels per tube.  This will speed up calculations.
  e. **Mask file** – One can choose a mask file for detailed calculations or calculations of coverage for sample environments that limit the range of scattered neutrons.  Most autoreduced data from linear position sensitive detector tube (LPSD) instruments will have the ends of the detector tubes masked.  One can use an autoreduced \*.nxs vanadium calibration file or prior autoreduced \*.nxs file for a mask file.  You can ask the instrument team to provide these files if you do not have them.  One can ask the instrument team for a mask file for complicated sample environments.  
  f. **Axes**  - The *Axis0*, *Axis1*, and *Axis2* variables are listed in a table.  These correspond to the image shown to the right of the table.  This image can be clicked on and rotated to view the different orientations.   The Axes panel consists of a table to define the Name, Direction of rotation, Sense of rotation, Minimum angle of rotation, Maximum angle of rotation, and Step size of rotation for each defined Axis.  Nearly all of DGS measurements will only use psi angle rotation for the measurements which is shown in the axis image to the right of the table.  The default values for psi direction and sense are (0,1,0) and (1) respectively.

    For example, if one were rotating psi from 0 degrees to 90 degrees in steps of 10 degrees one would enter minimum = 0, maximum = 90, and step = 10 in the Axes table for the Psi axis (Axis0).

  g. **Sample Parameters** - To calculate the detector coverage in reciprocal space, one needs to enter the orientation of the sample with respect to the instrument coordinates.  The local contact will work with you to help determine your experimental values for the orientation information.  One can use proposed values with the u and v vector formalism to determine detector coverage before the experiment begins.
  
    * Option 1 – Lattice parameters and u and v vectors
    
      1. **a**, **b**, and **c** are the lattice length parameters in units of Angstroms.  **alpha**, **beta**, and **gamma** are the lattice angle parameters in units of degrees.
      2. **u** and **v** vectors – The u and v vectors describe two reciprocal space vectors that lie in the equatorial scattering plane of the instrument such that uXv points vertically upward.  The components of the u and v vectors do not need to be integers.

    * Option 2 –the **UB matrix** – The UB matrix contains both orientation information and crystal structure information to define the orientation of the sample with respect to the instrument.   One can Load the UB matrix information directly using either the **LoadIsawUB** or **LoadNexusUB** buttons to load the information from the respective file types.

  h. **Plot Axes** – The Plot Axes part of the window is used to describe the area you would like plotted to test the detector coverage.   

     1. Start by entering the **Projection Basis** vectors, **Projection u**, **Projection v**, **Projection w**.  (note this u is different than the orientation vector u).  These are the reciprocal space vectors in which the detector coverage will be calculated and plotted.  Some common examples are [u=(1,0,0) v=(0,1,0) w=(0,0,1)] and [u=(1,0,0) v=(0,1,1) w=(0, 1,-1)] and [u=(1,1,0), v=(1,-1,0) w=(0,0,1)]. Note that changing the projection basis vectors automatically change the names of the plotting axes.
     2. The first two coordinates in the Projection table are the x and y coordinates for the detector coverage plot.  You can change these coordinates using the pull-down menus.  Enter the minimum and maximum values you would like the figure to have these values presented.  Also, enter the step size you would like the values presented in the output window. Step size is mandatory. If left empty, the default minimum and maximum values are used.
     3. The last two coordinates are the ranges of integration to use for the detector coverage calculation.  Not entering any values in these coordinate windows will integrate over the entire range of detector coverage available for those respective coordinates.
     4. **Plot** – the plot button starts the calculation and plots the output of detector coverage in the plot window.
     5. **Overplot** – will overplot an additional detector coverage calculation so that one can compare two or more configurations in the plot window.
     6. **Color by angle** – have this checked if you would like the coverage calculation to color each angle of rotation a different color.  If you are using the default  “viridis” colormap, blue corresponds to the first angle of rotation, and yellow will correspond to the last angle of the rotation scan.
     7. **Aspect ratio 1:1** – have this checked if you would like the reciprocal space aspect ratio to be plotted according to the respective lengths of the reciprocal space vectors used for the Projection Basis.
     8. **?** – click this for more information
     9. **Save Figure** – A dialog box will appear where one can save an image of the coverage figure which was made.


Examples
++++++++
Example 1
---------
Detector coverage for a crystal with :math:`a=b=6.28 \AA,` :math:`c= 12.56\AA,` :math:`\alpha=\beta=90^\circ,` :math:`\gamma=120^\circ,` with the sample with the `110` and `001` Bragg peaks in the scattering plane.  Find the measured range of Energy transfer (for positive values of energy transfers) as a function of the `00L` axis for `H=0.4` to `0.6` and `K` from `0.4` to `0.6` reciprocal lattice units For `Ei=60 meV` for the ARCS instrument for a sample rotation of 360 degrees. Solution is shown in :numref:`dgs-example1`.

.. plot_gui:: dgs_picture generate_picture dgs_planner_example1.png
   :name: dgs-example1
   :align: center
   :function_parameters: {"Instrument":"ARCS", "Ei":60, "psi_min":0, "psi_max":360, "psi_step":10.0, "a":6.28, "b":6.28, "c":12.56, "gamma":120, "u":"1,1,0", "v":"0,0,1", "e_min":0, "e_max":60, "proj_u_min":0.4,  "proj_u_max":0.6, "proj_v_min":0.4,  "proj_v_max":0.6, "dimension_order":[2,3,0,1]}

   Solution to Example 1. Note that the step size used for the Psi rotation in the example is set to a 10 degree step.  This is so that one can get a sense of the range of coverage without having to calculate the detector trajectories for every individual angle of the rotation.





