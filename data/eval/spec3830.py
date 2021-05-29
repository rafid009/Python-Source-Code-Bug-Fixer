import numpy as np 

def function(x):

	q0 = 7
	q2 = 1
	paths = []
	try:
		if x < 4:
			x = 0+x
			x = x/3
			q2 = 8*q2
			paths.append(1)
		else:
			q2 = q2*4
			q2 = q2+4
			q2 = 8*q0
			paths.append(2)
		if x > 5:
			q2 = q2+3
			paths.append(3)
		else:
			q2 = q0+q0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))