import numpy as np 

def function(x):

	q0 = x
	b3 = 8
	paths = []
	try:
		if x > 5:
			q0 = 1*2
			paths.append(1)
		else:
			x = x/b3
			b3 = 0-x
			paths.append(2)
		if b3 >= 6:
			x = 8*b3
			b3 = 9+b3
			b3 = 1+q0
			paths.append(3)
		else:
			x = x/b3
			q0 = x-2
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		x = b3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))