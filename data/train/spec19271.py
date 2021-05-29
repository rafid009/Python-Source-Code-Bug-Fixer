import numpy as np 

def function(x):

	d8 = x
	j1 = x
	paths = []
	try:
		if x >= 8:
			d8 = d8-j1
			j1 = j1*x
			paths.append(1)
		else:
			x = 5-x
			paths.append(2)
		if x > 0:
			x = 0+8
			x = x+j1
			paths.append(3)
		else:
			x = x*7
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