import numpy as np 

def function(x):

	x2 = x
	q1 = x
	paths = []
	try:
		if x >= 5:
			x = x2*8
			paths.append(1)
		else:
			x = x+7
			x = x/6
			q1 = 1+q1
			paths.append(2)
		if q1 < 4:
			x = x+4
			q1 = 3*q1
			q1 = q1-x
			paths.append(3)
		else:
			x = x2-x
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		x2 = q1**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))