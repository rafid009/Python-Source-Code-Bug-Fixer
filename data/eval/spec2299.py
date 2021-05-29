import numpy as np 

def function(x):

	f8 = x
	q1 = x
	paths = []
	try:
		if x >= 9:
			q1 = f8-q1
			paths.append(1)
		else:
			q1 = q1*q1
			q1 = 2/q1
			f8 = f8/2
			paths.append(2)
		if f8 > 3:
			f8 = f8+8
			paths.append(3)
		else:
			x = x+0
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		x = f8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))