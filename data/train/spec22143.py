import numpy as np 

def function(x):

	x0 = 5
	d5 = 5
	paths = []
	try:
		if d5 <= 4:
			d5 = 0-d5
			x = 7*1
			x0 = d5/x0
			paths.append(1)
		else:
			d5 = x*x0
			paths.append(2)
		if d5 < 7:
			x = x/8
			d5 = d5+x0
			d5 = d5-d5
			paths.append(3)
		else:
			d5 = x-d5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))