import numpy as np 

def function(x):

	k2 = x
	i9 = 2
	paths = []
	try:
		if i9 <= 4:
			x = 1+x
			x = 2+x
			x = x-8
			paths.append(1)
		else:
			k2 = k2+8
			k2 = x*k2
			paths.append(2)
		if k2 > 8:
			i9 = i9*7
			i9 = i9-9
			k2 = k2-x
			paths.append(3)
		else:
			k2 = k2/4
			x = x+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))