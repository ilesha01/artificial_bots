# artificial_bots


## Table of Contents

1. [How To Run The Code](https://github.com/ilesha-sawarkar/artificial_bots/blob/3D_generated_child_generations/README.md#1--how-to-run-the-code) 

2. [Details About The Code](https://github.com/ilesha-sawarkar/artificial_bots/blob/3D_generated_child_generations/README.md#2-details-about-the-code)
3. [Random Shapes Generated](https://github.com/ilesha-sawarkar/artificial_bots/blob/3D_generated_child_generations/README.md#3-random-shapes-generated)
4. [Generation of Body](https://github.com/ilesha-sawarkar/artificial_bots/blob/3D_generated_child_generations/README.md#4-generation-of-body)
5. [Generation of Brain](https://github.com/ilesha-sawarkar/artificial_bots/blob/3D_generated_child_generations/README.md#4-generation-of-body)
6. [Animation of 3D Evolving Creature](https://github.com/ilesha-sawarkar/artificial_bots/blob/3D_generated_child_generations/README.md#6-animation-of-3d-creature)
7. [Fitness Function](https://github.com/ilesha-sawarkar/artificial_bots/blob/3D_generated_child_generations/README.md#4-fitness-function)
8. [Generation of children] ()
9. [Citations](https://github.com/ilesha-sawarkar/artificial_bots/blob/3D_generated_child_generations/README.md#5-citations-for-references-used-to-buil-this-project)

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
   * Below is the flowchart depicting the generation of brains.

   <img width="873" alt="Screenshot 2023-02-20 at 11 22 51 PM" src="https://user-images.githubusercontent.com/114837040/220254859-ca949f50-d940-45d5-b417-80a99e521fd5.png">
   
## 6. Generation of Children
   * For the Generation of children we check whether the child can be created or not first
   * We generate the body and brain of the child based on the parent.
   * Links are added and deleted based on how fast or slow the robot is evolving



## 7. Animation of 3D Creature
   * [Youtube Link](https://youtu.be/iVttcKXFOvs)
   
   
   * Example of the 3D Creature generated
   
   <img width="814" alt="Screenshot 2023-02-20 at 10 16 27 PM" src="https://user-images.githubusercontent.com/114837040/220246470-70a84778-34e6-45b4-a17b-44154798a56f.png">
   
## 8.Fitness Graphs
   * At each instance the fitness graphs can be generated with numpyseed and randomseed
   * Fitness Graph=1, numpyseed=96, randomseed= 15
   
   ![Figure_1_npseed 96 rs 15](https://user-images.githubusercontent.com/114837040/221771531-4b2e5725-6d5f-4166-98f6-08020904b786.png)
   
   * Fitness Graph=2, numpyseed=40, randomseed= 5
![Figure_1_npseed 40 rs 5](https://user-images.githubusercontent.com/114837040/221771610-893396ba-4d31-46f2-91b5-5216df8f3b93.png)

   * Fitness Graph=3, numpyseed=40, randomseed= 20
![Figure_1npseed 40 rd 20](https://user-images.githubusercontent.com/114837040/221771715-fb328e18-c767-459b-ae9b-657fec6d563f.png)

   

## 8. Fitness Function
   * The fitness function at each generation is updating the parent's fitness by check the best fitness value for each of its child. The best fitness value of the child is taken as a new parent to generate more children at the the next generation.
   * The fitness function helps evolve the morphology to walk in x-coordinate direction by taking xPosition in the Get_Fitness() in the robot.py file.
   * Additionally the fitness function also takes in the coordinates of the world object and finds the associate difference in distance at each evolution to ensure the creature moves closer to the objects in the world.

## 8. References used to build this project
   *  [LudoBots](https://www.reddit.com/r/ludobots/wiki/installation/)
   *  [Pyrosim](https://github.com/jbongard/pyrosim)
