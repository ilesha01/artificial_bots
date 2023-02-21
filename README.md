# artificial_bots


## Table of Contents

1. [How To Run The Code](https://github.com/ilesha-sawarkar/artificial_bots/blob/kinematic_snake/README.md#1--how-to-run-the-code) 

2. [Details About The Code](https://github.com/ilesha-sawarkar/artificial_bots/blob/kinematic_snake/README.md#2-details-about-the-code)
3. [Random Shapes Generated](https://github.com/ilesha-sawarkar/artificial_bots/blob/kinematic_snake/README.md#3-random-shapes-generated)
4. [Generation of Body](https://github.com/ilesha-sawarkar/artificial_bots/blob/Random-3D-Creature/README.md#4-generation-of-body)
5. [Generation of Brain](https://github.com/ilesha-sawarkar/artificial_bots/blob/Random-3D-Creature/README.md#4-generation-of-body)
6. [Animation of 3D Creature](https://github.com/ilesha-sawarkar/artificial_bots/blob/Random-3D-Creature/README.md#6-animation-of-3d-creature)
7. [Fitness Function](https://github.com/ilesha-sawarkar/artificial_bots/blob/kinematic_snake/README.md#4-fitness-function)
8. [Citations](https://github.com/ilesha-sawarkar/artificial_bots/blob/kinematic_snake/README.md#5-citations-for-references-used-to-buil-this-project)

---------------------------------------------------------------------------------------------------------------------------------------------------------

## 1.  How To Run The Code 

   To run the code just run the program search.py after cloning the repository to your local machine.


   Another option is to run the code "python3 search.py" from the terminal or command line window. Run this command after using cd and runnning this command from the directory where you have stored your cloned repository on your local machine.
   


## 2. Details About The Code

  * The code generate random morphologies by linking them using joints.
  * It starts with the function Create_Body() where a random number of links is decided for the morphology.
  * Following which a list of randomly placed 0's and 1's are generated that depict the sensor values of the morphology.
  * Using this information we visually seperate the **links with sensors** as *Green* and the **links without sensors** as *Blue*.
  * **Additionally:**
    * I have also added a *randomization of dimensions* at each link.
   
  * In the Create_Brain()
     * The list of sensors and motors are used to generate synapses and adjust the weights of each neuron.
     * Sensor and motor neurons are named as per the naming pattern followed in the function Create_Body().


## 3. Random Shapes Generated

  * The generated morphologies are made of three types of shapes:
     * Cube
     * Cuboid - *Elongated Cube*
    
  * These morphologies are generated by random dimensions for the length, width and height.
  
## 4. Generation of Body
   * Initially a matrix is created to find all possible empty spaces in the 3d morphospace.
   * If there is space in the world a cube or cuboid is added. 
   * Accordingly the height, width, length is calculated with respect to each dimension and cuboidal space.
   * Pictographical representation of links and joints
   <img width="789" alt="Screenshot 2023-02-20 at 11 06 59 PM" src="https://user-images.githubusercontent.com/114837040/220252820-6dd4acd9-4b14-4f60-a826-e7f6d3a6f101.png">

    
   * Below is the 3D Creature generated by the above positioning of cubes:
     <img width="441" alt="Screenshot 2023-02-20 at 11 06 08 PM" src="https://user-images.githubusercontent.com/114837040/220252645-7671ce8b-e035-4910-9cc3-e97b2810a3dc.png">

## 5. Generation of Brain
   * For the Generation of Brain first we calculate the total number of sensors in the data by counting the 1's.
   * We already have a count of the motor Neurons by simpling appending the name of the joint Link after creation to the motor Neuron list.
   * After which we send a sensor neuron to each joint created.
   * We can then iterate and adjust the weights which are used to Send the synapse(movement) to the joints


## 6. Animation of 3D Creature
   * [Youtube Link](https://youtu.be/iVttcKXFOvs)
   
   <iframe width="560" height="315" src="https://www.youtube.com/embed/iVttcKXFOvs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen>
   
   
   * Example of the 3D Creature generated
   
   <img width="814" alt="Screenshot 2023-02-20 at 10 16 27 PM" src="https://user-images.githubusercontent.com/114837040/220246470-70a84778-34e6-45b4-a17b-44154798a56f.png">
   

## 7. Fitness Function
   * The fitness function at each generation is updating the parent's fitness by check the best fitness value for each of its child. The best fitness value of the child is taken as a new parent to generate more children at the the next generation.
   * The fitness function helps evolve the morphology to walk in x-coordinate direction by taking xPosition in the Get_Fitness() in the robot.py file.

## 8. References used to build this project
   *  [LudoBots](https://www.reddit.com/r/ludobots/wiki/installation/)
   *  [Pyrosim](https://github.com/jbongard/pyrosim)
