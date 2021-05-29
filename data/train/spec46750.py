import numpy as np 

def function(x):

	x2 = x
	q2 = 1
	x = 6
	paths = []
	try:
		if x2 <= 3:
			x = 3/q2
			x = x+5
			q2 = 4/q2
			paths.append(1)
		else:
			x2 = x/x2
			paths.append(2)
		if q2 < 6:
			x = x*8
			paths.append(3)
		else:
			q2 = q2/5
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x = x2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))