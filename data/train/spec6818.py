import numpy as np 

def function(x):

	n7 = 6
	d5 = 9
	paths = []
	try:
		if x >= 6:
			x = d5*x
			d5 = 5/4
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if x <= 5:
			n7 = n7-0
			n7 = n7-9
			paths.append(3)
		else:
			d5 = d5*5
			x = x*2
			x = d5*d5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))