import numpy as np 

def function(x):

	e8 = 2
	d6 = 6
	x = x
	paths = []
	try:
		if d6 >= 5:
			e8 = e8/x
			paths.append(1)
		else:
			x = 2/x
			d6 = 9/d6
			paths.append(2)
		if x < 0:
			x = 2-7
			paths.append(3)
		else:
			e8 = e8/3
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		x = e8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))