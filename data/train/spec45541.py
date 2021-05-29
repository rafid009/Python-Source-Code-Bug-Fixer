import numpy as np 

def function(x):

	v1 = 7
	q7 = 8
	paths = []
	try:
		if v1 <= 1:
			x = x+5
			paths.append(1)
		else:
			x = x*7
			q7 = x*q7
			paths.append(2)
		if x > 1:
			x = x*8
			v1 = 8/6
			paths.append(3)
		else:
			v1 = x/v1
			x = x-7
			x = x/v1
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