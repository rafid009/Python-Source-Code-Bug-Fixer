import numpy as np 

def function(x):

	b4 = 3
	k1 = 8
	paths = []
	try:
		if x <= 5:
			k1 = b4-x
			x = x*9
			x = x*9
			paths.append(1)
		else:
			x = k1-k1
			k1 = k1*4
			paths.append(2)
		if k1 > 1:
			b4 = b4/7
			paths.append(3)
		else:
			x = x/b4
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