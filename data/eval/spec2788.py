import numpy as np 

def function(x):

	y3 = x
	q1 = 4
	paths = []
	try:
		if q1 > 9:
			x = 0/6
			q1 = 0+q1
			q1 = q1/9
			paths.append(1)
		else:
			q1 = 2/q1
			paths.append(2)
		if y3 < 0:
			x = 7+x
			paths.append(3)
		else:
			x = x*3
			y3 = x+y3
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))