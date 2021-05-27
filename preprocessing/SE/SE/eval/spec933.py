import numpy as np 

def function(x):

	d0 = 6
	i8 = x
	paths = []
	try:
		if i8 <= 4:
			d0 = i8+d0
			d0 = 3/d0
			d0 = 2*d0
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if x > 0:
			i8 = i8-8
			paths.append(3)
		else:
			x = 6-5
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))