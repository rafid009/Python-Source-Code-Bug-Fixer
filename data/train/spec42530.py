import numpy as np 

def function(x):

	d4 = x
	k1 = x
	paths = []
	try:
		if d4 < 9:
			x = x-5
			x = x-4
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if d4 > 3:
			x = 6/4
			k1 = 5+k1
			x = 4/2
			paths.append(3)
		else:
			x = 3-d4
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		x = k1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))