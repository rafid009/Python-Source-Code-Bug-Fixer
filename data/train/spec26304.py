import numpy as np 

def function(x):

	k6 = x
	d6 = x
	x = x
	paths = []
	try:
		if k6 <= 0:
			d6 = d6-d6
			paths.append(1)
		else:
			d6 = x/d6
			x = 4-5
			x = x+k6
			paths.append(2)
		if x <= 9:
			k6 = k6*4
			paths.append(3)
		else:
			d6 = 5/d6
			d6 = 6/d6
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