.. _testpage:

=====================
Tests for python code
=====================

.. contents::
  :local:

Test 1
######

This is just a figure, produced at buildtime

.. plot::
   :include-source:
   
   # This figure is a test
   import numpy as np
   import matplotlib.pyplot as plt
   
   x = np.arange(11)
   y = x**2
   
   fig, ax = plt.subplots()
   ax.plot(x, y)
   #fig.show()
   
Test 2
######

This is just a test for rendering MathJax

.. math::
  :label: eq1

  y = ax^2 +\beta+\AA


Test 3
######

.. testcode::

   1+1         # this will give no output!
   print(2+2)  # this will give output

.. testoutput::

   4
   
Test 4
######
Test with setup

.. testsetup:: test4

   import sys

.. testcode:: test4

   print('/usr/lib/python3/dist-packages' in sys.path)

.. testoutput:: test4

   True


Test 5
######
Test GUI plot

.. figure:: images/fig.png
   :name: my-custom-label
   :height: 300
   :width: 500
   :align: center
   
   some caption
   

The awesome :numref:`my-custom-label` is not related to :eq:`eq1`

.. plot_gui:: dgs_picture generate_picture dgs_planner_fig1.png
   :name: f2
   :width: 500
   :align: center
      
   awesome caption





Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus a euismod ex, vitae sollicitudin mauris. Maecenas quis mauris a quam egestas dignissim. Nullam vel massa non nibh gravida mollis tincidunt quis ligula. Sed sodales est nec tortor fermentum finibus. Nam non placerat erat, et dignissim nisl. Ut sed nisi eget dolor sollicitudin eleifend. Donec justo turpis, hendrerit vel orci ac, iaculis malesuada nisi. Integer dictum odio sed lacus lobortis egestas. Donec non gravida nibh, vel rhoncus elit. Ut sed eros placerat, aliquam felis id, tincidunt sapien. Aliquam vitae aliquet massa. Nullam suscipit lectus ut sem dapibus, ac sollicitudin massa ullamcorper. Ut ex lacus, egestas interdum rhoncus in, lacinia in est. Sed ut justo neque. Phasellus arcu libero, scelerisque consectetur laoreet quis, fermentum sed orci. Quisque vitae ornare nulla.

Integer est elit, fermentum a egestas non, pellentesque tempor libero. Aliquam erat volutpat. Morbi at enim orci. Sed id arcu ipsum. Phasellus lobortis mi nec blandit convallis. Nullam ac molestie nibh, id malesuada orci. In eu lacus felis. Etiam posuere elit vel enim venenatis pretium. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Donec neque est, maximus in magna blandit, euismod vehicula justo. Morbi tempus erat nisi, sollicitudin fermentum sapien vehicula quis. Quisque vel finibus odio, vitae finibus quam. Vivamus magna augue, viverra quis faucibus sed, finibus id leo. Donec ut dui ut urna tempus aliquam.

Proin hendrerit aliquet odio, in efficitur sapien pulvinar non. Cras imperdiet vitae tellus non bibendum. Integer augue sapien, ultricies in nisi id, fringilla fermentum augue. Aenean mattis dolor id risus vestibulum tristique. Donec vel turpis cursus, commodo libero nec, congue velit. Duis at mattis lorem. Nulla ut orci est.

Nam dui leo, luctus a elit et, eleifend interdum eros. Cras pharetra, lorem ut tincidunt luctus, quam diam feugiat odio, non vehicula lacus orci aliquam nisi. Sed fermentum erat ut orci pellentesque bibendum. Praesent sed purus eros. Donec libero nulla, finibus sit amet quam ac, auctor dictum ligula. Nulla facilisi. Proin imperdiet ornare bibendum. Proin volutpat dui lobortis odio sagittis, non cursus ex vehicula. Phasellus consequat, mauris eget imperdiet malesuada, arcu enim viverra enim, ac molestie tortor justo a orci. Duis vel fringilla metus. Mauris eleifend dolor a felis auctor, a pulvinar augue tincidunt. Ut ut odio scelerisque, luctus est quis, interdum ante. Donec nec diam ac velit pretium vestibulum. Nulla lobortis dapibus dolor, vel iaculis eros hendrerit et. Etiam mattis pharetra justo vel ornare.

Nam facilisis efficitur turpis vel varius. In sit amet erat in leo pharetra feugiat. Donec in dui purus. Praesent nec quam risus. Proin quis dui mauris. Donec pellentesque odio sed felis rutrum vestibulum. Sed pharetra nunc ac felis viverra aliquet. 


Done with :numref:`f2`

