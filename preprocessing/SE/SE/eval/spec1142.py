import numpy as np 

def function(x):

	q1 = x
	r3 = 5
	paths = []
	try:
		if x >= 7:
			q1 = q1/x
			x = 2-x
			q1 = 5-8
			paths.append(1)
		else:
			x = 1+4
			paths.append(2)
		if x >= 2:
			r3 = 7*r3
			x = 4+r3
			paths.append(3)
		else:
			q1 = q1/4
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		r3 = q1**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))