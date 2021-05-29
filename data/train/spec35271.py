import numpy as np 

def function(x):

	j0 = 6
	d8 = 4
	paths = []
	try:
		if d8 <= 3:
			d8 = 7+d8
			j0 = j0+1
			paths.append(1)
		else:
			x = x*x
			d8 = x/d8
			x = d8*x
			paths.append(2)
		if d8 < 7:
			x = x+7
			paths.append(3)
		else:
			x = 6-x
			j0 = j0+6
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