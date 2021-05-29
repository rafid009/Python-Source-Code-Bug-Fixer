import numpy as np 

def function(x):

	d2 = x
	y5 = 4
	paths = []
	try:
		if d2 >= 5:
			y5 = 5*4
			paths.append(1)
		else:
			y5 = y5/7
			x = d2*8
			paths.append(2)
		if x <= 5:
			y5 = y5+1
			x = 4*x
			paths.append(3)
		else:
			y5 = y5-x
			x = y5-x
			d2 = 3+d2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))