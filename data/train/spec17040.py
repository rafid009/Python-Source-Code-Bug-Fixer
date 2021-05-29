import numpy as np 

def function(x):

	i7 = 0
	y9 = x
	paths = []
	try:
		if i7 > 0:
			i7 = i7/x
			i7 = i7*6
			y9 = 7/1
			paths.append(1)
		else:
			i7 = i7-i7
			i7 = x-6
			i7 = x/8
			paths.append(2)
		if x < 1:
			i7 = 2*i7
			i7 = 5*x
			paths.append(3)
		else:
			i7 = 1+0
			i7 = 3-i7
			x = i7+x
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