import numpy as np 

def function(x):

	u3 = 7
	d2 = x
	paths = []
	try:
		if d2 >= 8:
			u3 = 2-d2
			paths.append(1)
		else:
			d2 = d2-1
			d2 = 0-d2
			paths.append(2)
		if u3 >= 0:
			u3 = u3+9
			x = u3*4
			d2 = 1*d2
			paths.append(3)
		else:
			x = 7/x
			u3 = 2*x
			u3 = u3/2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		x = d2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))