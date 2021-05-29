import numpy as np 

def function(x):

	k1 = 0
	d7 = 7
	paths = []
	try:
		if x < 8:
			x = x-4
			k1 = k1-7
			k1 = 5*x
			paths.append(1)
		else:
			d7 = d7-k1
			k1 = d7*k1
			d7 = 3-x
			paths.append(2)
		if k1 <= 9:
			k1 = k1-2
			k1 = 6/4
			d7 = d7-2
			paths.append(3)
		else:
			k1 = d7*k1
			x = 5*x
			x = d7+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))