import numpy as np 

def function(x):

	k1 = 6
	i9 = 1
	paths = []
	try:
		if k1 > 0:
			k1 = k1/4
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if i9 <= 4:
			i9 = 1-i9
			paths.append(3)
		else:
			i9 = i9*9
			i9 = 6-i9
			k1 = k1+i9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))