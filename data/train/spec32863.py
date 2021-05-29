import numpy as np 

def function(x):

	b2 = 4
	k0 = x
	paths = []
	try:
		if x < 8:
			k0 = b2*6
			b2 = b2*7
			paths.append(1)
		else:
			x = x-9
			k0 = k0-1
			b2 = x-6
			paths.append(2)
		if b2 <= 5:
			k0 = k0+7
			x = 4/9
			x = x+7
			paths.append(3)
		else:
			k0 = k0*5
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		x = b2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))