import numpy as np 

def function(x):

	j6 = 8
	s9 = x
	paths = []
	try:
		if j6 >= 1:
			x = 7/x
			j6 = j6-x
			paths.append(1)
		else:
			j6 = j6*3
			paths.append(2)
		if x > 9:
			s9 = 9/s9
			paths.append(3)
		else:
			j6 = 0*j6
			s9 = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))