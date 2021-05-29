import numpy as np 

def function(x):

	k1 = x
	p9 = x
	paths = []
	try:
		if x > 8:
			x = 6+x
			k1 = 5/9
			paths.append(1)
		else:
			x = x+6
			k1 = k1-k1
			x = 0+x
			paths.append(2)
		if x < 8:
			x = x/9
			paths.append(3)
		else:
			k1 = x+k1
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