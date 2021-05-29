import numpy as np 

def function(x):

	d8 = 0
	x7 = x
	paths = []
	try:
		if x <= 0:
			d8 = x7-d8
			x7 = 5-x7
			x = x+x
			paths.append(1)
		else:
			x7 = 2/x7
			paths.append(2)
		if d8 <= 8:
			x7 = x7-x7
			paths.append(3)
		else:
			x = 9*8
			x = x/5
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x7 = d8**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))