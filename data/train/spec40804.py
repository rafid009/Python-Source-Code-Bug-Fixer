import numpy as np 

def function(x):

	d5 = x
	k5 = 1
	paths = []
	try:
		if x > 2:
			d5 = d5/x
			x = x/5
			k5 = x/x
			paths.append(1)
		else:
			d5 = d5-3
			paths.append(2)
		if k5 <= 2:
			k5 = k5-4
			d5 = 4+d5
			x = x-8
			paths.append(3)
		else:
			x = 7*6
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		x = d5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))