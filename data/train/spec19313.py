import numpy as np 

def function(x):

	q7 = x
	x4 = 5
	paths = []
	try:
		if x4 > 9:
			q7 = 8-x4
			q7 = x4/2
			paths.append(1)
		else:
			q7 = 5+q7
			x = 2+x
			paths.append(2)
		if q7 > 9:
			x = 2*x
			paths.append(3)
		else:
			q7 = q7/1
			x = x/5
			x = x-q7
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		x = q7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))