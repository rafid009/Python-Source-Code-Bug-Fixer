import numpy as np 

def function(x):

	b8 = x
	q2 = x
	paths = []
	try:
		if x <= 1:
			b8 = b8*6
			paths.append(1)
		else:
			b8 = b8/2
			q2 = q2-5
			b8 = 7/b8
			paths.append(2)
		if q2 <= 4:
			x = x*6
			b8 = q2-x
			paths.append(3)
		else:
			b8 = x/q2
			q2 = q2/x
			b8 = b8*3
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))