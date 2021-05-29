import numpy as np 

def function(x):

	n4 = 3
	f0 = x
	paths = []
	try:
		if f0 > 7:
			f0 = f0*5
			paths.append(1)
		else:
			f0 = f0+7
			paths.append(2)
		if x > 5:
			x = 5/5
			paths.append(3)
		else:
			n4 = 0+x
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