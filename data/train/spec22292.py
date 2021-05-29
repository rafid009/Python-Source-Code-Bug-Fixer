import numpy as np 

def function(x):

	d8 = 9
	w6 = x
	paths = []
	try:
		if w6 > 4:
			w6 = x*1
			d8 = x-6
			paths.append(1)
		else:
			d8 = d8*x
			paths.append(2)
		if x <= 0:
			x = 7/x
			paths.append(3)
		else:
			d8 = 0*d8
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))