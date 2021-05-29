import numpy as np 

def function(x):

	v2 = x
	d2 = x
	paths = []
	try:
		if x <= 1:
			v2 = v2+4
			paths.append(1)
		else:
			v2 = 9-1
			d2 = d2*x
			paths.append(2)
		if x >= 1:
			d2 = 2-d2
			x = 9+v2
			d2 = 6/d2
			paths.append(3)
		else:
			d2 = 7+2
			v2 = x*4
			d2 = v2*5
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		x = v2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))