import numpy as np 

def function(x):

	q7 = x
	v7 = x
	paths = []
	try:
		if q7 <= 9:
			v7 = 4-v7
			paths.append(1)
		else:
			v7 = v7*3
			v7 = x/v7
			paths.append(2)
		if q7 < 1:
			q7 = 8+q7
			paths.append(3)
		else:
			v7 = 4-1
			x = x/q7
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		q7 = q7**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))