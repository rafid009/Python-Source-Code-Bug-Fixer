import numpy as np 

def function(x):

	b1 = 1
	n5 = 6
	paths = []
	try:
		if b1 <= 5:
			b1 = 8*4
			paths.append(1)
		else:
			n5 = 9-7
			x = x*1
			b1 = 1*b1
			paths.append(2)
		if b1 >= 5:
			b1 = b1*3
			paths.append(3)
		else:
			x = x-x
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