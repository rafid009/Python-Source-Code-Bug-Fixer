import numpy as np 

def function(x):

	d1 = x
	w6 = x
	paths = []
	try:
		if x > 3:
			x = x-8
			paths.append(1)
		else:
			w6 = x-w6
			x = w6+x
			x = 8/d1
			paths.append(2)
		if w6 <= 2:
			w6 = 0*w6
			w6 = w6*x
			paths.append(3)
		else:
			d1 = x-d1
			w6 = 9+2
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))