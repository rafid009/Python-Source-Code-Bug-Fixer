import numpy as np 

def function(x):

	d6 = 3
	e3 = x
	paths = []
	try:
		if x >= 1:
			d6 = 8*4
			e3 = 9/d6
			paths.append(1)
		else:
			d6 = 2+d6
			e3 = 2*x
			paths.append(2)
		if x <= 8:
			d6 = 1/d6
			e3 = e3+7
			d6 = d6/d6
			paths.append(3)
		else:
			d6 = 5-d6
			x = x/d6
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))