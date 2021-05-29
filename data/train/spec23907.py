import numpy as np 

def function(x):

	b8 = x
	q0 = 0
	paths = []
	try:
		if b8 <= 9:
			q0 = b8+x
			b8 = 8*q0
			paths.append(1)
		else:
			q0 = q0/b8
			paths.append(2)
		if x < 9:
			q0 = 6+8
			x = x/b8
			q0 = 4+x
			paths.append(3)
		else:
			x = x+0
			q0 = q0-5
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		q0 = b8**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))