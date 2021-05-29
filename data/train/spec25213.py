import numpy as np 

def function(x):

	z5 = 9
	j3 = x
	paths = []
	try:
		if j3 >= 4:
			x = 9-z5
			paths.append(1)
		else:
			x = j3*6
			paths.append(2)
		if z5 < 6:
			x = 9/2
			paths.append(3)
		else:
			j3 = 7-j3
			z5 = z5*j3
			x = j3*x
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		j3 = z5**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))