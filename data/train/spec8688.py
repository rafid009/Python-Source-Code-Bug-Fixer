import numpy as np 

def function(x):

	d9 = x
	d7 = 5
	paths = []
	try:
		if d7 <= 1:
			d9 = 5+d9
			paths.append(1)
		else:
			d7 = x-d7
			paths.append(2)
		if x >= 1:
			d7 = d9*0
			d9 = 8+d9
			paths.append(3)
		else:
			d9 = d9-d7
			x = 4*7
			d9 = d9-3
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x = d7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))