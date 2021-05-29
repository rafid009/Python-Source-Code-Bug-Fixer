import numpy as np 

def function(x):

	k5 = x
	f0 = 0
	paths = []
	try:
		if x > 8:
			x = 8+x
			k5 = k5/8
			x = 0/3
			paths.append(1)
		else:
			k5 = f0+k5
			x = x-4
			paths.append(2)
		if k5 < 8:
			x = x-8
			x = 6*4
			paths.append(3)
		else:
			f0 = f0-f0
			f0 = 5-f0
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