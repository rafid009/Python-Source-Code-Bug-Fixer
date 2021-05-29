import numpy as np 

def function(x):

	d9 = 9
	d6 = x
	paths = []
	try:
		if d9 < 6:
			x = x/7
			x = 7-5
			paths.append(1)
		else:
			d9 = d9/x
			paths.append(2)
		if x < 4:
			d6 = d6-3
			x = x-x
			d6 = d6/4
			paths.append(3)
		else:
			d9 = 5*d9
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		x = d6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))