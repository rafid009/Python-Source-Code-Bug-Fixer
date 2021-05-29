import numpy as np 

def function(x):

	k7 = 7
	x1 = 8
	paths = []
	try:
		if x1 >= 7:
			k7 = 5-x1
			paths.append(1)
		else:
			k7 = 0+k7
			k7 = x-5
			k7 = k7*8
			paths.append(2)
		if x < 7:
			k7 = 8/k7
			x = x-6
			x1 = 2-1
			paths.append(3)
		else:
			x = x/8
			k7 = x*k7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k7 = x**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))