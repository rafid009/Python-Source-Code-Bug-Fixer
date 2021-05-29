import numpy as np 

def function(x):

	s9 = 0
	j7 = 3
	x = 0
	paths = []
	try:
		if x > 6:
			j7 = 7/8
			paths.append(1)
		else:
			s9 = s9/j7
			x = 8*j7
			j7 = 3+j7
			paths.append(2)
		if x > 4:
			x = 4+7
			x = s9-8
			s9 = 4*x
			paths.append(3)
		else:
			x = x-x
			j7 = s9-j7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j7 = x**0.5
		return j7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))