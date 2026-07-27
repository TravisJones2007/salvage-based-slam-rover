# Dev Log
#General Progress Reporting

(Entries Categorized by date and work session)

##2026-07-26 
-Project Pivot + Python Refresher-

Restarted project with new direction. Earlier this summer i started to develop and explore an ambitious autonomous rover project
which would have included articulated arms, a locking suspension system, among many other sophisticated systems(seprate rpo), but due to
many factors including moving to a new location, losing access to a working 3d printer, reliable power and internet, the scope i desired
simply turned out to be too difficult. i have restarted the project by pivoting to something i can actually build, using for the most part,
hardware i already own, that being a differential drive SLAM rover built from a salvaged ender 3 neo max 3D printer, developed off grid on 
solar/battery power under a tight budget and time constraints

Project Log
-Refreshed Python fundamentals after extended time away from the platform, worked through a myriad of small exercises to refresh my memory, which
in additon can be carried over to real rover tasks, they are as follows:
-differential-drive kinematics
-LiDAR scan filtering
-G-code command string generation
- a teleop control loop
- a Robot class with state and methods
  in addition:
 - Ordered the RPLIDAR C1 (360°, 12m, DTOF)
 - Confirmed the salvaged Ender 3 control board and stepper motors work by driving them over serial with G code from my laptop

   Struggled with:
   -Rusty on Python mechanics after months off
   -classes were not covered in my university python course, so i had to learn them from scratch
   - f strings and enumerate were also new to me

   Learned:
   class states and methods in python, structures and general framework of ROS2 architecture

   Next:
   start ROS2 fundamentals while the LIDAR ships
   
