import numpy as np 

def function(x):

	d7 = x
	e5 = 3
	paths = []
	try:
		if e5 < 7:
			d7 = 2+d7
			e5 = e5/8
			paths.append(1)
		else:
			x = x/4
			paths.append(2)
		if x <= 7:
			e5 = e5-x
			paths.append(3)
		else:
			e5 = 2/d7
			e5 = d7*e5
			e5 = e5-6
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