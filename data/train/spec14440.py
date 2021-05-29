import numpy as np 

def function(x):

	d0 = x
	q7 = 4
	paths = []
	try:
		if x < 4:
			x = x/7
			paths.append(1)
		else:
			q7 = q7/4
			paths.append(2)
		if d0 <= 2:
			d0 = d0/1
			paths.append(3)
		else:
			q7 = q7*d0
			x = x/3
			x = x*3
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