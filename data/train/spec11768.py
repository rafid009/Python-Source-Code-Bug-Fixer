import numpy as np 

def function(x):

	q4 = x
	b1 = 8
	paths = []
	try:
		if x > 0:
			x = x/5
			paths.append(1)
		else:
			q4 = 2-8
			paths.append(2)
		if x < 5:
			q4 = q4-8
			x = x*4
			paths.append(3)
		else:
			x = 9+3
			b1 = 6*b1
			q4 = 0*q4
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		x = q4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))