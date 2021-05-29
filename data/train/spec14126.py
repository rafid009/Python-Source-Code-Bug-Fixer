import numpy as np 

def function(x):

	u8 = x
	n1 = 5
	paths = []
	try:
		if n1 <= 1:
			x = 4+3
			paths.append(1)
		else:
			n1 = n1*x
			paths.append(2)
		if n1 <= 6:
			u8 = 1-u8
			paths.append(3)
		else:
			u8 = 9-u8
			x = x-7
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		x = u8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))