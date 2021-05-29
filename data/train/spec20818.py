import numpy as np 

def function(x):

	j0 = x
	h3 = 9
	x = 7
	paths = []
	try:
		if h3 > 2:
			h3 = 2+h3
			x = 6*x
			paths.append(1)
		else:
			x = 4+h3
			x = x+h3
			x = j0+j0
			paths.append(2)
		if j0 > 1:
			x = j0*x
			h3 = j0-3
			paths.append(3)
		else:
			j0 = 4+j0
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		j0 = h3**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))