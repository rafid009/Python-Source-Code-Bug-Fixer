import numpy as np 

def function(x):

	w3 = 1
	d9 = 6
	paths = []
	try:
		if d9 >= 3:
			d9 = d9/x
			paths.append(1)
		else:
			d9 = 1/d9
			paths.append(2)
		if w3 > 9:
			d9 = 6+w3
			x = x/6
			paths.append(3)
		else:
			w3 = w3/6
			w3 = x/d9
			w3 = 2/w3
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		x = d9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))