import numpy as np 

def function(x):

	d9 = x
	x7 = 6
	paths = []
	try:
		if x > 2:
			x = x/1
			x = 1/3
			d9 = d9/1
			paths.append(1)
		else:
			d9 = 4+2
			paths.append(2)
		if x7 < 2:
			x = x*7
			x7 = x7+0
			paths.append(3)
		else:
			d9 = d9/5
			x7 = 2-x7
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))