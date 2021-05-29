import numpy as np 

def function(x):

	b8 = 4
	q6 = 8
	paths = []
	try:
		if x <= 2:
			q6 = x+1
			b8 = x+b8
			q6 = q6-1
			paths.append(1)
		else:
			x = 1/8
			paths.append(2)
		if x < 6:
			q6 = 4*q6
			b8 = x-0
			q6 = q6*6
			paths.append(3)
		else:
			x = 5+x
			b8 = 6/1
			q6 = 3/4
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