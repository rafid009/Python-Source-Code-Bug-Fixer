import numpy as np 

def function(x):

	b1 = 8
	u1 = 7
	paths = []
	try:
		if u1 <= 1:
			b1 = 7*b1
			paths.append(1)
		else:
			b1 = b1/6
			b1 = b1-4
			paths.append(2)
		if x < 4:
			b1 = 4-u1
			b1 = 7+b1
			b1 = 7-b1
			paths.append(3)
		else:
			x = u1/x
			b1 = 4-b1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))