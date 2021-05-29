import numpy as np 

def function(x):

	x2 = x
	d1 = 7
	x = 5
	paths = []
	try:
		if x <= 2:
			x = x-2
			x2 = d1-8
			paths.append(1)
		else:
			d1 = 6+d1
			x2 = x2*9
			paths.append(2)
		if x > 1:
			x = x/4
			x = x+d1
			paths.append(3)
		else:
			x2 = x2+7
			x = x+9
			x = 7/4
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x = x2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))