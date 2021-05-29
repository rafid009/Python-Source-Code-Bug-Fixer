import numpy as np 

def function(x):

	q2 = x
	v5 = 9
	paths = []
	try:
		if q2 <= 3:
			x = x-8
			x = x+2
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if q2 < 1:
			x = q2*x
			paths.append(3)
		else:
			v5 = 0/3
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