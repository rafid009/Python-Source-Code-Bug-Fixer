import numpy as np 

def function(x):

	q5 = 8
	y8 = x
	x = 2
	paths = []
	try:
		if q5 >= 0:
			q5 = 0-8
			paths.append(1)
		else:
			x = 4-x
			y8 = 0-y8
			paths.append(2)
		if y8 < 6:
			q5 = q5+9
			y8 = x*y8
			paths.append(3)
		else:
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))