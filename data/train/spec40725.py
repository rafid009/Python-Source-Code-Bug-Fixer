import numpy as np 

def function(x):

	d6 = x
	t0 = 8
	paths = []
	try:
		if x <= 1:
			x = x/2
			d6 = t0-d6
			paths.append(1)
		else:
			d6 = 1*2
			d6 = 8/1
			d6 = d6*t0
			paths.append(2)
		if d6 > 9:
			x = x/6
			paths.append(3)
		else:
			d6 = 0+d6
			d6 = t0-x
			d6 = d6+x
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