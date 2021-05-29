import numpy as np 

def function(x):

	i9 = 1
	k7 = x
	x = x
	paths = []
	try:
		if i9 > 0:
			i9 = 2*3
			i9 = x/6
			i9 = k7*k7
			paths.append(1)
		else:
			k7 = k7*4
			paths.append(2)
		if k7 < 0:
			x = 7*x
			paths.append(3)
		else:
			x = x*4
			i9 = x-i9
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		i9 = k7**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))