import numpy as np 

def function(x):

	j1 = 6
	w3 = 3
	paths = []
	try:
		if w3 < 9:
			j1 = j1*0
			x = x-j1
			paths.append(1)
		else:
			j1 = 4*j1
			x = x/2
			paths.append(2)
		if w3 < 4:
			j1 = 2-j1
			j1 = 6/j1
			paths.append(3)
		else:
			x = 8-x
			j1 = j1+8
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