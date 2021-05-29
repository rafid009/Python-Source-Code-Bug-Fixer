import numpy as np 

def function(x):

	d7 = 3
	r5 = 9
	paths = []
	try:
		if x >= 9:
			d7 = d7*4
			r5 = r5/2
			paths.append(1)
		else:
			r5 = r5*d7
			paths.append(2)
		if d7 >= 0:
			d7 = x+d7
			r5 = 5-r5
			r5 = d7+r5
			paths.append(3)
		else:
			r5 = r5+2
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