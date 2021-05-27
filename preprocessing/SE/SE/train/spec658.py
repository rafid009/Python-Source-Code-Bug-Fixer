import numpy as np 

def function(x):

	d0 = 3
	k5 = 4
	paths = []
	try:
		if x < 2:
			x = 4+5
			paths.append(1)
		else:
			d0 = 5-k5
			k5 = d0-8
			d0 = 4/k5
			paths.append(2)
		if x >= 3:
			d0 = 3/9
			x = k5/x
			x = x*7
			paths.append(3)
		else:
			x = x+d0
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		x = k5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))