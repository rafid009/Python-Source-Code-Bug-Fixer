import numpy as np 

def function(x):

	b7 = 1
	q0 = 9
	x = x
	paths = []
	try:
		if q0 <= 3:
			q0 = q0/6
			paths.append(1)
		else:
			b7 = x/3
			q0 = q0/6
			x = x/1
			paths.append(2)
		if b7 >= 8:
			x = x*q0
			b7 = b7+3
			paths.append(3)
		else:
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		b7 = b7**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))