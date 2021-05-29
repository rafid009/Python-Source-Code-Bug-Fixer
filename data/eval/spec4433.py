import numpy as np 

def function(x):

	b0 = x
	i9 = x
	x = x
	paths = []
	try:
		if b0 < 5:
			b0 = i9+2
			paths.append(1)
		else:
			i9 = i9/4
			b0 = b0-3
			paths.append(2)
		if i9 >= 4:
			b0 = b0+0
			i9 = 5+x
			paths.append(3)
		else:
			i9 = i9/4
			b0 = b0+i9
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