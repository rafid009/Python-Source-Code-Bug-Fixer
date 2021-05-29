import numpy as np 

def function(x):

	k1 = 7
	d7 = 3
	paths = []
	try:
		if x > 4:
			d7 = x*d7
			k1 = 7+k1
			paths.append(1)
		else:
			k1 = 6-k1
			d7 = 5*7
			paths.append(2)
		if k1 <= 0:
			x = x*6
			d7 = d7*5
			x = 1/x
			paths.append(3)
		else:
			x = x*4
			k1 = 8-5
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