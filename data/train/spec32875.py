import numpy as np 

def function(x):

	d8 = 7
	w3 = x
	paths = []
	try:
		if d8 <= 8:
			w3 = w3-1
			paths.append(1)
		else:
			x = x+w3
			x = x+0
			d8 = 8+6
			paths.append(2)
		if w3 <= 4:
			w3 = d8-x
			paths.append(3)
		else:
			w3 = 8+w3
			x = x/6
			x = 3+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))