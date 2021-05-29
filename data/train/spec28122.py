import numpy as np 

def function(x):

	q6 = 2
	r7 = 8
	paths = []
	try:
		if x >= 6:
			r7 = r7-x
			r7 = q6-3
			x = x+6
			paths.append(1)
		else:
			q6 = x/q6
			paths.append(2)
		if x < 7:
			r7 = 1-r7
			x = 2*1
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		q6 = r7**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))