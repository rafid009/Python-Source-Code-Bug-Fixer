import numpy as np 

def function(x):

	j6 = 6
	w3 = 7
	paths = []
	try:
		if x <= 3:
			j6 = j6+w3
			paths.append(1)
		else:
			j6 = j6*2
			w3 = 2/j6
			paths.append(2)
		if j6 <= 8:
			w3 = 1/w3
			paths.append(3)
		else:
			x = j6/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w3 = x**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))