import numpy as np 

def function(x):

	k9 = 3
	h1 = 4
	paths = []
	try:
		if k9 <= 3:
			k9 = k9+2
			x = x-5
			k9 = h1+9
			paths.append(1)
		else:
			k9 = k9-6
			paths.append(2)
		if k9 >= 4:
			x = x+x
			k9 = 2+k9
			k9 = 0+3
			paths.append(3)
		else:
			k9 = k9*8
			k9 = k9+3
			x = 2+k9
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