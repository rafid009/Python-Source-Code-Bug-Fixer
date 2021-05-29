import numpy as np 

def function(x):

	a9 = 5
	d1 = 3
	paths = []
	try:
		if x <= 1:
			a9 = a9+x
			d1 = x/9
			d1 = d1*2
			paths.append(1)
		else:
			a9 = x*6
			a9 = d1/d1
			paths.append(2)
		if a9 > 7:
			d1 = 9/d1
			paths.append(3)
		else:
			a9 = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))