import numpy as np 

def function(x):

	x3 = x
	j6 = x
	paths = []
	try:
		if x >= 6:
			x3 = x3-x
			x3 = 6*x3
			x = x3-9
			paths.append(1)
		else:
			j6 = x*4
			paths.append(2)
		if x >= 8:
			x = x+x3
			x = x/x
			j6 = j6*j6
			paths.append(3)
		else:
			x3 = 2*x3
			x3 = x3*4
			paths.append(4)
		paths.append(5)
		assert j6 >= 0
		j6 = j6**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))