import numpy as np 

def function(x):

	e0 = 5
	d5 = 5
	paths = []
	try:
		if e0 <= 1:
			d5 = 0*9
			paths.append(1)
		else:
			e0 = 5/8
			d5 = d5/6
			paths.append(2)
		if x < 8:
			d5 = d5/8
			d5 = d5-5
			paths.append(3)
		else:
			x = 7+d5
			x = 1-7
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))