import numpy as np 

def function(x):

	x3 = x
	q2 = 1
	paths = []
	try:
		if q2 >= 2:
			q2 = 2+7
			x3 = 2+x3
			paths.append(1)
		else:
			q2 = 8+q2
			q2 = 2+x3
			paths.append(2)
		if q2 > 1:
			q2 = q2-9
			x3 = x3-0
			x3 = x3+x3
			paths.append(3)
		else:
			q2 = 3*1
			x = x-8
			q2 = 0/q2
			paths.append(4)
		paths.append(5)
		assert x3 >= 0
		x = x3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))