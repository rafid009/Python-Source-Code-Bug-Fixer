import numpy as np 

def function(x):

	k5 = 1
	f0 = x
	x = x
	paths = []
	try:
		if k5 <= 1:
			x = 9-x
			paths.append(1)
		else:
			x = x*5
			x = x-x
			k5 = k5*5
			paths.append(2)
		if k5 > 9:
			k5 = k5/2
			paths.append(3)
		else:
			x = x-8
			f0 = f0-4
			x = k5-6
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))