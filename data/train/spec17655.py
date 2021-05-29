import numpy as np 

def function(x):

	n6 = x
	b8 = 1
	x = x
	paths = []
	try:
		if n6 <= 7:
			b8 = b8-6
			b8 = 8+b8
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if n6 <= 8:
			x = x/5
			paths.append(3)
		else:
			n6 = n6*8
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))