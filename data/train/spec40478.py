import numpy as np 

def function(x):

	x1 = x
	d6 = 0
	paths = []
	try:
		if d6 >= 0:
			x1 = x1-4
			x1 = x1*x
			paths.append(1)
		else:
			x1 = 4+x1
			x = x+9
			x = 8+9
			paths.append(2)
		if x >= 9:
			d6 = d6-x1
			paths.append(3)
		else:
			d6 = d6*5
			paths.append(4)
		paths.append(5)
		assert x1 >= 0
		x1 = x1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))