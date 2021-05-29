import numpy as np 

def function(x):

	f8 = x
	k6 = 3
	paths = []
	try:
		if f8 >= 5:
			x = 3-7
			paths.append(1)
		else:
			k6 = x-7
			paths.append(2)
		if x >= 2:
			x = x+6
			f8 = k6/4
			paths.append(3)
		else:
			x = 8-0
			k6 = 5*k6
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		k6 = k6**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))