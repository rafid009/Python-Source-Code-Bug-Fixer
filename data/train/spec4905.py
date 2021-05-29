import numpy as np 

def function(x):

	y5 = 0
	d5 = 9
	paths = []
	try:
		if d5 < 3:
			x = 4+x
			y5 = y5+d5
			paths.append(1)
		else:
			y5 = 0*d5
			paths.append(2)
		if y5 > 8:
			d5 = d5*7
			x = x+1
			paths.append(3)
		else:
			y5 = x+7
			d5 = y5/6
			y5 = 4+y5
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