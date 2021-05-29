import numpy as np 

def function(x):

	q0 = x
	b3 = x
	paths = []
	try:
		if x > 2:
			b3 = 5+b3
			q0 = 2-7
			q0 = b3-1
			paths.append(1)
		else:
			b3 = q0/b3
			x = 7/3
			q0 = q0*3
			paths.append(2)
		if b3 < 8:
			b3 = b3+x
			x = x/5
			b3 = 9*q0
			paths.append(3)
		else:
			x = 9+7
			q0 = 9-x
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