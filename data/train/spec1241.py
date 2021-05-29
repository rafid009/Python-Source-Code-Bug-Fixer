import numpy as np 

def function(x):

	b1 = x
	q0 = x
	paths = []
	try:
		if x < 9:
			x = b1/4
			b1 = x*b1
			b1 = x*q0
			paths.append(1)
		else:
			b1 = x+b1
			b1 = b1*4
			paths.append(2)
		if b1 < 3:
			q0 = 8/6
			paths.append(3)
		else:
			x = 8-x
			b1 = 0*b1
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))