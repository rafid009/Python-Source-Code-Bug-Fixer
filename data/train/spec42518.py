import numpy as np 

def function(x):

	h4 = x
	j0 = x
	paths = []
	try:
		if x < 6:
			j0 = 4*j0
			paths.append(1)
		else:
			h4 = 2-4
			paths.append(2)
		if x < 1:
			j0 = j0-1
			h4 = j0-9
			h4 = h4/9
			paths.append(3)
		else:
			h4 = 0*9
			h4 = 1*h4
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		j0 = h4**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))