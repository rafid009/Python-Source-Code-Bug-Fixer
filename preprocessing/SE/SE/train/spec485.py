import numpy as np 

def function(x):

	k9 = x
	d7 = 2
	x = 3
	paths = []
	try:
		if k9 < 5:
			d7 = x-5
			d7 = 4/d7
			paths.append(1)
		else:
			k9 = k9+9
			x = x*7
			d7 = 4*d7
			paths.append(2)
		if k9 < 9:
			x = x*k9
			x = x-7
			paths.append(3)
		else:
			x = 4-x
			k9 = k9+d7
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