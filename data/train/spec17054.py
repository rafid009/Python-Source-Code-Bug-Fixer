import numpy as np 

def function(x):

	b9 = x
	q0 = 9
	paths = []
	try:
		if q0 <= 7:
			b9 = 5-q0
			b9 = b9+b9
			q0 = q0+9
			paths.append(1)
		else:
			q0 = q0+9
			q0 = q0*3
			q0 = q0*b9
			paths.append(2)
		if q0 >= 0:
			x = 9*6
			b9 = 5-x
			q0 = q0+5
			paths.append(3)
		else:
			b9 = b9*7
			q0 = q0*5
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