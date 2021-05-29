import numpy as np 

def function(x):

	d7 = 7
	k9 = x
	paths = []
	try:
		if k9 < 0:
			x = x-7
			d7 = d7*9
			paths.append(1)
		else:
			d7 = k9/d7
			paths.append(2)
		if d7 > 9:
			k9 = 2+k9
			d7 = 7*d7
			d7 = 8-d7
			paths.append(3)
		else:
			d7 = d7+k9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d7 = x**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))