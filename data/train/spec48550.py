import numpy as np 

def function(x):

	b1 = x
	b2 = x
	paths = []
	try:
		if b1 > 1:
			x = 7-x
			b2 = 7+b2
			b2 = 3*b2
			paths.append(1)
		else:
			b1 = 1*5
			b2 = x+b2
			paths.append(2)
		if b2 > 2:
			b1 = b1/3
			paths.append(3)
		else:
			b1 = b1-b2
			b1 = b2-x
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		b2 = b1**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))