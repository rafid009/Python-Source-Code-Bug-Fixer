import numpy as np 

def function(x):

	g5 = 7
	b7 = 2
	paths = []
	try:
		if x < 7:
			x = b7/x
			x = x/4
			paths.append(1)
		else:
			x = 6+x
			b7 = 8/6
			paths.append(2)
		if g5 > 0:
			x = x-g5
			x = x/7
			paths.append(3)
		else:
			x = 6/x
			b7 = 9*g5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))