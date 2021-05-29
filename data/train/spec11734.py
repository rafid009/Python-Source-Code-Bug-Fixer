import numpy as np 

def function(x):

	f0 = 9
	x2 = 8
	paths = []
	try:
		if f0 > 8:
			f0 = 5-f0
			paths.append(1)
		else:
			x = x-x
			f0 = x2*3
			x2 = 7/8
			paths.append(2)
		if f0 <= 4:
			f0 = x2*3
			paths.append(3)
		else:
			x2 = x2*x2
			f0 = f0+1
			x2 = 4/f0
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