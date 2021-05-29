import numpy as np 

def function(x):

	x5 = 9
	b2 = x
	x = x
	paths = []
	try:
		if b2 >= 9:
			x = x*5
			x = 7-x
			paths.append(1)
		else:
			b2 = b2+x
			paths.append(2)
		if b2 >= 1:
			b2 = 2/b2
			b2 = x5/b2
			paths.append(3)
		else:
			x = 3/x
			x5 = 8*1
			b2 = 8+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b2 = x**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))