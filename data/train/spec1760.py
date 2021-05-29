import numpy as np 

def function(x):

	q2 = x
	y5 = 7
	paths = []
	try:
		if y5 >= 2:
			x = x+x
			x = 0-x
			paths.append(1)
		else:
			y5 = 2*y5
			q2 = 5+7
			q2 = 0/q2
			paths.append(2)
		if y5 < 3:
			y5 = y5+0
			paths.append(3)
		else:
			x = x-q2
			y5 = x/5
			q2 = q2/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))