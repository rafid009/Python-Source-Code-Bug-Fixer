import numpy as np 

def function(x):

	d8 = 0
	w9 = x
	x = 7
	paths = []
	try:
		if d8 < 6:
			d8 = w9+8
			paths.append(1)
		else:
			d8 = d8/1
			paths.append(2)
		if d8 < 1:
			w9 = d8/7
			w9 = w9*0
			paths.append(3)
		else:
			x = x/d8
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))