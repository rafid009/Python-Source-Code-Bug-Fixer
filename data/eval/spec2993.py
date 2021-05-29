import numpy as np 

def function(x):

	t4 = x
	d6 = x
	paths = []
	try:
		if d6 < 8:
			d6 = d6*9
			d6 = 0+d6
			x = x/6
			paths.append(1)
		else:
			x = 5+7
			x = x*x
			x = 3-x
			paths.append(2)
		if d6 > 8:
			x = 5+x
			d6 = 3+d6
			d6 = 6-d6
			paths.append(3)
		else:
			d6 = 8*5
			x = x/5
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