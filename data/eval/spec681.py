import numpy as np 

def function(x):

	n5 = x
	b8 = x
	paths = []
	try:
		if n5 >= 7:
			n5 = n5/b8
			n5 = n5-3
			paths.append(1)
		else:
			b8 = b8*1
			b8 = 1*5
			x = b8/x
			paths.append(2)
		if b8 >= 7:
			x = 9-x
			b8 = b8-3
			x = 1+x
			paths.append(3)
		else:
			b8 = x-5
			b8 = 6*b8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n5 = x**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))