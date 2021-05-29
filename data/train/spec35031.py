import numpy as np 

def function(x):

	b0 = 5
	q2 = 4
	paths = []
	try:
		if q2 >= 0:
			q2 = x/q2
			q2 = x/2
			q2 = q2/7
			paths.append(1)
		else:
			x = 4*x
			paths.append(2)
		if b0 >= 6:
			q2 = q2/6
			paths.append(3)
		else:
			q2 = x+q2
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		x = q2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))