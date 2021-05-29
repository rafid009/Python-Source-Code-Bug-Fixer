import numpy as np 

def function(x):

	s9 = x
	g4 = 4
	paths = []
	try:
		if s9 > 0:
			s9 = 1*s9
			paths.append(1)
		else:
			g4 = g4*1
			paths.append(2)
		if x < 3:
			g4 = 8/g4
			paths.append(3)
		else:
			x = x*g4
			x = x/g4
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))