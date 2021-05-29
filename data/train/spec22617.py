import numpy as np 

def function(x):

	i7 = x
	h4 = 8
	paths = []
	try:
		if x >= 3:
			x = i7/2
			i7 = i7-4
			paths.append(1)
		else:
			h4 = h4*x
			paths.append(2)
		if i7 >= 7:
			h4 = h4/5
			i7 = i7/3
			h4 = 0*h4
			paths.append(3)
		else:
			i7 = i7*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))