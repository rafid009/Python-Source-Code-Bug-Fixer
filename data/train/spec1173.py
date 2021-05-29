import numpy as np 

def function(x):

	x7 = 1
	b4 = 0
	paths = []
	try:
		if b4 > 5:
			x7 = 9+4
			x7 = b4*5
			paths.append(1)
		else:
			b4 = b4+b4
			paths.append(2)
		if b4 >= 8:
			x = x*4
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))