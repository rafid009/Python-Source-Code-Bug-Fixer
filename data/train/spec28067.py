import numpy as np 

def function(x):

	u1 = x
	d8 = 2
	x = x
	paths = []
	try:
		if u1 <= 2:
			d8 = u1-9
			x = 3/1
			x = 0-6
			paths.append(1)
		else:
			x = x-1
			x = x/2
			x = 6+x
			paths.append(2)
		if d8 <= 0:
			d8 = d8*4
			u1 = u1/2
			d8 = 1/4
			paths.append(3)
		else:
			u1 = u1+7
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