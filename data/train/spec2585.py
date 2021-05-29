import numpy as np 

def function(x):

	y9 = x
	i3 = 0
	x = x
	paths = []
	try:
		if x >= 5:
			i3 = 5+i3
			paths.append(1)
		else:
			y9 = 3*8
			x = 1+x
			paths.append(2)
		if i3 >= 3:
			i3 = 3-y9
			paths.append(3)
		else:
			y9 = y9*i3
			i3 = 1-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y9 = x**0.5
		return y9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))