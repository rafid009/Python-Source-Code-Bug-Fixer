import numpy as np 

def function(x):

	j0 = 2
	w3 = x
	paths = []
	try:
		if j0 >= 8:
			x = 6/7
			x = x-1
			paths.append(1)
		else:
			x = x+8
			x = x-6
			j0 = w3*5
			paths.append(2)
		if w3 >= 1:
			w3 = 8+w3
			paths.append(3)
		else:
			j0 = x+w3
			w3 = w3-x
			w3 = 7-w3
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))