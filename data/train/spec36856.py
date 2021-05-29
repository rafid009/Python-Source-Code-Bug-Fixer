import numpy as np 

def function(x):

	w3 = x
	e3 = x
	paths = []
	try:
		if e3 >= 4:
			w3 = w3*4
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if w3 <= 9:
			w3 = w3-x
			paths.append(3)
		else:
			w3 = w3/2
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		w3 = e3**0.5
		return w3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))