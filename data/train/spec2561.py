import numpy as np 

def function(x):

	b3 = x
	n8 = 8
	paths = []
	try:
		if b3 >= 3:
			b3 = b3*0
			paths.append(1)
		else:
			b3 = 8/6
			paths.append(2)
		if b3 > 3:
			x = 2*7
			paths.append(3)
		else:
			n8 = n8*n8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))