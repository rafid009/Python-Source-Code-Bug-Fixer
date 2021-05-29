import numpy as np 

def function(x):

	x8 = 2
	b5 = 7
	x = x
	paths = []
	try:
		if x <= 0:
			x8 = x+x8
			b5 = b5*x8
			b5 = b5*x
			paths.append(1)
		else:
			x8 = 1+x8
			paths.append(2)
		if b5 < 1:
			x = 3-x
			paths.append(3)
		else:
			x8 = 7-x8
			b5 = b5/2
			x8 = x8*1
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))