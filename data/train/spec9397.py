import numpy as np 

def function(x):

	x7 = x
	f0 = 9
	paths = []
	try:
		if f0 < 4:
			x7 = x7-x7
			f0 = f0+8
			paths.append(1)
		else:
			x7 = f0*x
			paths.append(2)
		if f0 > 1:
			f0 = 6+3
			f0 = x7-f0
			f0 = f0+9
			paths.append(3)
		else:
			x = x-x
			x7 = 4+x7
			x7 = x7*8
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))