import numpy as np 

def function(x):

	f6 = x
	d7 = x
	paths = []
	try:
		if x < 9:
			d7 = d7/5
			paths.append(1)
		else:
			f6 = f6*x
			f6 = 5+x
			paths.append(2)
		if f6 < 7:
			x = 9+x
			d7 = 6/1
			paths.append(3)
		else:
			d7 = 5/f6
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