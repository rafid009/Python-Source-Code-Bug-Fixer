import numpy as np 

def function(x):

	f0 = 8
	u2 = 4
	paths = []
	try:
		if x <= 1:
			f0 = f0-f0
			x = x*u2
			paths.append(1)
		else:
			f0 = u2+f0
			paths.append(2)
		if x >= 2:
			u2 = x*u2
			paths.append(3)
		else:
			f0 = 4-f0
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