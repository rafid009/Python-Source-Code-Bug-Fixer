import numpy as np 

def function(x):

	k5 = 3
	e9 = 7
	paths = []
	try:
		if k5 > 7:
			x = 1+x
			k5 = k5*0
			paths.append(1)
		else:
			e9 = e9+7
			e9 = e9+e9
			k5 = k5-5
			paths.append(2)
		if e9 > 8:
			e9 = k5+x
			paths.append(3)
		else:
			e9 = e9-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k5 = x**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))