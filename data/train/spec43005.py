import numpy as np 

def function(x):

	d8 = 5
	f1 = 6
	paths = []
	try:
		if f1 >= 1:
			d8 = d8*3
			x = 8*x
			d8 = f1*x
			paths.append(1)
		else:
			d8 = d8-d8
			paths.append(2)
		if x > 9:
			x = d8-4
			f1 = 7+3
			d8 = x+d8
			paths.append(3)
		else:
			d8 = 2+d8
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