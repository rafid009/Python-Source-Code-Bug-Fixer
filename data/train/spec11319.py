import numpy as np 

def function(x):

	k9 = 3
	h3 = x
	paths = []
	try:
		if k9 > 5:
			k9 = 0-h3
			x = x/6
			paths.append(1)
		else:
			h3 = x-h3
			x = 9+x
			paths.append(2)
		if h3 <= 2:
			x = 1+x
			x = x*k9
			paths.append(3)
		else:
			k9 = k9+0
			x = 6-x
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