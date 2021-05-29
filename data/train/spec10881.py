import numpy as np 

def function(x):

	k8 = x
	f7 = 8
	x = 2
	paths = []
	try:
		if k8 <= 8:
			f7 = x/f7
			paths.append(1)
		else:
			x = x+k8
			x = 0*f7
			paths.append(2)
		if k8 < 6:
			f7 = 4/x
			paths.append(3)
		else:
			f7 = 0*f7
			x = 0-3
			f7 = f7*5
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