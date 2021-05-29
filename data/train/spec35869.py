import numpy as np 

def function(x):

	j2 = 2
	h4 = x
	paths = []
	try:
		if x <= 0:
			h4 = h4+7
			paths.append(1)
		else:
			j2 = 3-2
			h4 = 9*h4
			x = x*7
			paths.append(2)
		if j2 > 5:
			h4 = x*7
			h4 = j2/h4
			x = x+1
			paths.append(3)
		else:
			x = h4+6
			j2 = h4*j2
			j2 = 1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))