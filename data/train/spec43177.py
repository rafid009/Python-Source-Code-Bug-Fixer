import numpy as np 

def function(x):

	i1 = 3
	w3 = 3
	paths = []
	try:
		if x > 0:
			w3 = w3*2
			x = x/4
			paths.append(1)
		else:
			i1 = i1-0
			i1 = w3/4
			w3 = w3-4
			paths.append(2)
		if x >= 4:
			i1 = 0+x
			paths.append(3)
		else:
			w3 = i1*w3
			i1 = i1/8
			i1 = 5*w3
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