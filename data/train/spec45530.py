import numpy as np 

def function(x):

	d7 = x
	f9 = 1
	paths = []
	try:
		if d7 < 6:
			x = d7/x
			x = 8*3
			d7 = x/d7
			paths.append(1)
		else:
			d7 = 7*4
			d7 = 5-d7
			paths.append(2)
		if d7 > 3:
			x = 4/x
			d7 = f9+2
			paths.append(3)
		else:
			d7 = 2*d7
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		f9 = d7**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))