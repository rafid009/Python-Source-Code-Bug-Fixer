import numpy as np 

def function(x):

	b7 = 4
	u3 = x
	paths = []
	try:
		if b7 < 6:
			u3 = b7/x
			x = x-0
			paths.append(1)
		else:
			b7 = 0-b7
			paths.append(2)
		if x > 8:
			x = b7/x
			b7 = b7-8
			x = 2*x
			paths.append(3)
		else:
			u3 = 0-3
			b7 = b7+4
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		b7 = u3**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))