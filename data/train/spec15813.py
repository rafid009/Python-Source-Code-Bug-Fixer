import numpy as np 

def function(x):

	k7 = 4
	b8 = 7
	paths = []
	try:
		if b8 <= 3:
			x = x/k7
			paths.append(1)
		else:
			b8 = b8-3
			b8 = b8/x
			x = x*7
			paths.append(2)
		if b8 > 9:
			k7 = 1*k7
			paths.append(3)
		else:
			b8 = 7*3
			k7 = k7+3
			b8 = b8+b8
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