import numpy as np 

def function(x):

	k0 = x
	q4 = 8
	paths = []
	try:
		if k0 > 9:
			x = 0+5
			q4 = k0-0
			q4 = 4+k0
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if x < 2:
			q4 = 6/3
			x = x+3
			x = x+x
			paths.append(3)
		else:
			x = 8*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k0 = x**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))