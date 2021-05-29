import numpy as np 

def function(x):

	e3 = x
	d5 = 6
	x = x
	paths = []
	try:
		if x >= 7:
			e3 = 1*e3
			e3 = e3/9
			d5 = 0+0
			paths.append(1)
		else:
			x = x+d5
			e3 = d5*7
			d5 = d5-8
			paths.append(2)
		if e3 <= 8:
			e3 = 4/4
			paths.append(3)
		else:
			d5 = 1-8
			x = 4+6
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