import numpy as np 

def function(x):

	b7 = x
	k1 = x
	paths = []
	try:
		if b7 < 6:
			b7 = b7-2
			x = 9*x
			x = 2/3
			paths.append(1)
		else:
			k1 = x/1
			paths.append(2)
		if b7 >= 3:
			k1 = 8+k1
			k1 = 9*k1
			x = 1+x
			paths.append(3)
		else:
			x = x+b7
			x = b7-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))