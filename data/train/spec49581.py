import numpy as np 

def function(x):

	w3 = 8
	j0 = x
	paths = []
	try:
		if j0 < 9:
			x = 9+4
			paths.append(1)
		else:
			x = x+9
			w3 = j0-9
			w3 = 3*w3
			paths.append(2)
		if w3 > 7:
			x = 1/x
			x = 7/9
			j0 = j0*w3
			paths.append(3)
		else:
			j0 = 7+1
			w3 = w3/5
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		w3 = j0**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))