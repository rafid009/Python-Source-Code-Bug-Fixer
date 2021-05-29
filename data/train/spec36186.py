import numpy as np 

def function(x):

	k1 = 2
	e5 = 3
	x = 3
	paths = []
	try:
		if x >= 0:
			x = x-x
			paths.append(1)
		else:
			e5 = e5/x
			paths.append(2)
		if e5 < 4:
			k1 = k1/3
			e5 = e5-5
			k1 = e5+1
			paths.append(3)
		else:
			k1 = k1-k1
			e5 = x+e5
			e5 = e5/3
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		e5 = k1**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))