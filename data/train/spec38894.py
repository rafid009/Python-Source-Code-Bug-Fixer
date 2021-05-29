import numpy as np 

def function(x):

	h1 = 2
	j0 = x
	paths = []
	try:
		if x > 0:
			j0 = 3/j0
			paths.append(1)
		else:
			j0 = j0+5
			h1 = h1+4
			x = 7+x
			paths.append(2)
		if j0 >= 3:
			j0 = j0/7
			paths.append(3)
		else:
			h1 = 4/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j0 = x**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))