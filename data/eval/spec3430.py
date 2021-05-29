import numpy as np 

def function(x):

	e9 = x
	d5 = x
	paths = []
	try:
		if x >= 0:
			e9 = 1+e9
			e9 = 3*e9
			d5 = 3*d5
			paths.append(1)
		else:
			x = x+x
			x = d5/9
			e9 = 5+7
			paths.append(2)
		if x <= 7:
			e9 = e9-1
			x = e9-x
			paths.append(3)
		else:
			x = 5/e9
			x = 4/x
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