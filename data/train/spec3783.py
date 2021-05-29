import numpy as np 

def function(x):

	d2 = 3
	b1 = x
	paths = []
	try:
		if b1 > 7:
			d2 = x+d2
			d2 = d2+d2
			paths.append(1)
		else:
			x = b1+2
			d2 = d2-3
			d2 = 1*b1
			paths.append(2)
		if x >= 4:
			x = x+7
			x = x*x
			d2 = d2-d2
			paths.append(3)
		else:
			d2 = b1/d2
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