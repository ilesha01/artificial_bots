#!/usr/bin/env python3

from sensor import SENSOR
from motor import MOTOR
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np 
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT :
	def __init__(self,solutionID):
		self.robotId = p.loadURDF(f"body/body{solutionID}.urdf")
		self.motors={}
		self.sensors={}
		
		self.nn = NEURAL_NETWORK(f"brain/brain{solutionID}.nndf")
		
		self.solutionID=solutionID
		
		os.system(f"rm brain/brain{self.solutionID}.nndf")
		os.system(f"rm body/body{self.solutionID}.urdf")
		pyrosim.Prepare_To_Simulate(self.robotId)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()

		
	def Prepare_To_Sense(self):
		#self.sensors=SENSOR()
		
		for linkName in pyrosim.linkNamesToIndices:
			#print(self.sensors)
			self.sensors[linkName] = SENSOR(linkName)
			#print(linkName)
			#print(self.sensors)
		
	def Sense(self, time):
		for linkName in pyrosim.linkNamesToIndices:
			#print(self.sensors)
			self.sensors[linkName].Get_Value(time)
			
			#print(linkName)

		
	def Prepare_To_Act(self):
		i=0
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)
			#self.motors[jointName].Prepare_To_Act()
			#self.motors[jointName].Set_Value(self.robotId, i)
			
			#print(c.am[i])
			i=i+1
		
		
	def Act(self,t):
		#print('Here')
		for neuronName in self.nn.Get_Neuron_Names():
			
			if self.nn.Is_Motor_Neuron(neuronName):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)    
				desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange   
				#print(jointName, desiredAngle)
				
				#print('Here Motors:',self.motors)
				self.motors[jointName].Set_Value(self.robotId, desiredAngle)
				
				
	
	def Think(self):
		self.nn.Update()
		#self.nn.Print()
		
		
	def Save_Values(self):
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName].Save_Values()
			
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName].Save_Values()
			
			#self.motors[jointName] = sensor.MOTOR(jointName)
	
	def Get_Fitness(self):
		basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
		basePosition = basePositionAndOrientation[0]
		xPosition = basePosition[0]
		fitness_file = open(f"data/tmp{self.solutionID}.txt", "w")
		fitness_file.write(str(xPosition))
		
		os.system(f"mv data/tmp{self.solutionID}.txt data/fitness{self.solutionID}.txt")
		fitness_file.close()
				