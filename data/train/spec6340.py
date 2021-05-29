import numpy as np 

def function(x):

	b1 = x
	n0 = x
	paths = []
	try:
		if x <= 5:
			b1 = n0-b1
			b1 = b1*9
			x = x-5
			paths.append(1)
		else:
			b1 = b1*5
			paths.append(2)
		if b1 > 7:
			b1 = 7-9
			b1 = b1-8
			paths.append(3)
		else:
			x = x/6
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))