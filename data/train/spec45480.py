import numpy as np 

def function(x):

	y4 = x
	d6 = x
	paths = []
	try:
		if d6 <= 0:
			y4 = y4*6
			d6 = 3+d6
			paths.append(1)
		else:
			d6 = 0*6
			paths.append(2)
		if x >= 3:
			y4 = y4/1
			paths.append(3)
		else:
			y4 = y4*d6
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))