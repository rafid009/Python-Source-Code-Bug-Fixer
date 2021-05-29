import numpy as np 

def function(x):

	h2 = x
	i1 = 0
	paths = []
	try:
		if i1 > 0:
			i1 = 0/i1
			h2 = 4-x
			paths.append(1)
		else:
			x = 7-x
			x = 7+x
			h2 = h2-i1
			paths.append(2)
		if x <= 0:
			h2 = h2/x
			paths.append(3)
		else:
			x = x/6
			x = x+i1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))