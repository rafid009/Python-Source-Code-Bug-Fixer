import numpy as np 

def function(x):

	y8 = x
	q1 = 4
	paths = []
	try:
		if x <= 5:
			x = x*1
			paths.append(1)
		else:
			q1 = 8+x
			paths.append(2)
		if x >= 0:
			y8 = 3-y8
			x = y8/8
			paths.append(3)
		else:
			y8 = y8-5
			q1 = q1+x
			y8 = 6+y8
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		q1 = y8**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))