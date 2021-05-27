import numpy as np 

def function(x):

	i9 = x
	r4 = x
	paths = []
	try:
		if x <= 2:
			x = x-x
			r4 = r4+0
			paths.append(1)
		else:
			r4 = r4*5
			x = r4-x
			paths.append(2)
		if x <= 7:
			i9 = i9*i9
			paths.append(3)
		else:
			x = x-3
			x = x/4
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		i9 = r4**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))