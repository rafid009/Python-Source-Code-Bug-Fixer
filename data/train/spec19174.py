import numpy as np 

def function(x):

	i9 = x
	k9 = x
	paths = []
	try:
		if k9 <= 7:
			x = x-5
			paths.append(1)
		else:
			i9 = x*x
			x = x*4
			x = x+3
			paths.append(2)
		if k9 < 4:
			k9 = k9+7
			paths.append(3)
		else:
			k9 = 3+k9
			i9 = i9*6
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