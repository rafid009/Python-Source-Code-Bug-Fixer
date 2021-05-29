import numpy as np 

def function(x):

	x9 = 6
	d5 = x
	x = 6
	paths = []
	try:
		if x > 5:
			x9 = 7+x9
			x = x/x9
			paths.append(1)
		else:
			x9 = 7-x9
			paths.append(2)
		if d5 > 3:
			x9 = x+x9
			paths.append(3)
		else:
			x = 8-3
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))