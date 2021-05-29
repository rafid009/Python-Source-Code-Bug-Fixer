import numpy as np 

def function(x):

	d7 = 3
	r8 = 6
	x = 3
	paths = []
	try:
		if d7 <= 4:
			r8 = r8/9
			x = r8*7
			paths.append(1)
		else:
			x = 6-9
			paths.append(2)
		if d7 <= 8:
			x = x-6
			paths.append(3)
		else:
			x = 5-9
			r8 = 0*r8
			d7 = 6*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))