import numpy as np 

def function(x):

	d9 = 6
	w6 = 9
	paths = []
	try:
		if d9 >= 2:
			w6 = w6-d9
			x = x+5
			x = x+w6
			paths.append(1)
		else:
			x = 6*8
			paths.append(2)
		if w6 >= 1:
			w6 = w6+2
			paths.append(3)
		else:
			x = 0+d9
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