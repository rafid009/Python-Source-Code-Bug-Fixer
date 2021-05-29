import numpy as np 

def function(x):

	k2 = x
	i7 = x
	paths = []
	try:
		if x > 1:
			x = 1/6
			x = 9/x
			i7 = i7-x
			paths.append(1)
		else:
			k2 = i7+2
			i7 = 4*i7
			x = x-k2
			paths.append(2)
		if i7 <= 1:
			x = x-x
			paths.append(3)
		else:
			x = 5-x
			x = 0*k2
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		x = i7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))