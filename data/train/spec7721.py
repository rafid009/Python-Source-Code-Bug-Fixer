import numpy as np 

def function(x):

	k7 = 6
	i6 = x
	paths = []
	try:
		if k7 > 5:
			x = x+k7
			x = 0-x
			paths.append(1)
		else:
			k7 = k7+3
			paths.append(2)
		if k7 <= 8:
			x = x+x
			paths.append(3)
		else:
			i6 = i6*k7
			i6 = 2/i6
			k7 = k7/6
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