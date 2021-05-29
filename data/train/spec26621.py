import numpy as np 

def function(x):

	i9 = 0
	k6 = x
	paths = []
	try:
		if k6 <= 0:
			x = 5*x
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if x >= 4:
			i9 = x*8
			paths.append(3)
		else:
			i9 = i9-0
			x = 8*7
			paths.append(4)
		paths.append(5)
		assert k6 >= 0
		x = k6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))