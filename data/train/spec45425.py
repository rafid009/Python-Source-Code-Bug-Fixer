import numpy as np 

def function(x):

	d1 = 1
	d7 = x
	paths = []
	try:
		if d7 <= 5:
			d1 = d7/d1
			d7 = d7/9
			d7 = 3-d7
			paths.append(1)
		else:
			d1 = d1*3
			paths.append(2)
		if x > 0:
			x = 6*2
			d1 = d1/x
			d1 = d1/5
			paths.append(3)
		else:
			d1 = x*d1
			x = x+2
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