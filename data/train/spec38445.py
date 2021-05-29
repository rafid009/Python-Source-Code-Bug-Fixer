import numpy as np 

def function(x):

	j0 = x
	z4 = 7
	paths = []
	try:
		if j0 >= 2:
			j0 = 8*9
			z4 = 4+x
			j0 = 0-j0
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if j0 > 5:
			x = j0+x
			j0 = 0/8
			paths.append(3)
		else:
			x = x*j0
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))