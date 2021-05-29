import numpy as np 

def function(x):

	e4 = x
	q1 = x
	paths = []
	try:
		if x < 3:
			x = 9*5
			paths.append(1)
		else:
			x = 7+x
			e4 = e4-8
			e4 = e4*1
			paths.append(2)
		if e4 < 2:
			q1 = q1*5
			q1 = q1+8
			paths.append(3)
		else:
			e4 = 5+e4
			x = 2-8
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		x = q1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))