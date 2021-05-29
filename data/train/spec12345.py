import numpy as np 

def function(x):

	k2 = x
	x6 = x
	paths = []
	try:
		if k2 >= 9:
			x = x+7
			paths.append(1)
		else:
			x6 = 4*5
			x = x-2
			k2 = k2+5
			paths.append(2)
		if x6 >= 3:
			x = 1-x
			paths.append(3)
		else:
			x6 = x6+x6
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x6 = k2**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))