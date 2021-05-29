import numpy as np 

def function(x):

	d2 = 4
	i6 = x
	paths = []
	try:
		if x <= 7:
			d2 = i6+d2
			d2 = 5*1
			paths.append(1)
		else:
			x = x*x
			d2 = x-x
			i6 = 9+x
			paths.append(2)
		if d2 > 9:
			d2 = d2/d2
			paths.append(3)
		else:
			i6 = i6*5
			x = 1+x
			i6 = i6*x
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