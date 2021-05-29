import numpy as np 

def function(x):

	i7 = 8
	k1 = x
	x = 0
	paths = []
	try:
		if k1 >= 3:
			i7 = x-7
			paths.append(1)
		else:
			k1 = 6-k1
			k1 = 3/2
			paths.append(2)
		if x >= 4:
			i7 = i7+7
			paths.append(3)
		else:
			k1 = 7*k1
			x = i7/5
			i7 = 8+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))