import numpy as np 

def function(x):

	b3 = x
	d2 = x
	paths = []
	try:
		if x > 3:
			b3 = b3*5
			d2 = b3-x
			x = 2*x
			paths.append(1)
		else:
			b3 = b3*b3
			paths.append(2)
		if d2 <= 4:
			x = 7-x
			b3 = 3+b3
			x = 3-8
			paths.append(3)
		else:
			x = x*5
			d2 = x+d2
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