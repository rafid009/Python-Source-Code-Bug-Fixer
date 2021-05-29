import numpy as np 

def function(x):

	k2 = x
	d6 = x
	paths = []
	try:
		if d6 > 6:
			k2 = k2+2
			paths.append(1)
		else:
			d6 = 4+k2
			paths.append(2)
		if d6 <= 1:
			x = k2+5
			k2 = 6*1
			paths.append(3)
		else:
			x = 4/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))