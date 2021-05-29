import numpy as np 

def function(x):

	v7 = 3
	s4 = 3
	x = 6
	paths = []
	try:
		if x >= 6:
			v7 = v7*v7
			s4 = 4-s4
			s4 = 5*x
			paths.append(1)
		else:
			x = 6*6
			v7 = 7+x
			paths.append(2)
		if v7 >= 0:
			x = x+4
			v7 = 2+5
			v7 = v7-9
			paths.append(3)
		else:
			v7 = 0+4
			s4 = x+9
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))