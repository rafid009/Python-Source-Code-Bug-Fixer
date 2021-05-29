import numpy as np 

def function(x):

	v5 = 1
	k7 = 3
	x = x
	paths = []
	try:
		if x >= 3:
			v5 = v5-2
			x = 9-x
			x = k7*x
			paths.append(1)
		else:
			v5 = 7*v5
			v5 = 4-v5
			x = x-4
			paths.append(2)
		if k7 >= 5:
			v5 = 1/v5
			k7 = 8+k7
			paths.append(3)
		else:
			k7 = x*v5
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