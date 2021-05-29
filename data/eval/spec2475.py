import numpy as np 

def function(x):

	u1 = 3
	q1 = x
	x = x
	paths = []
	try:
		if q1 > 0:
			u1 = 2-4
			paths.append(1)
		else:
			q1 = q1-5
			q1 = q1*4
			paths.append(2)
		if u1 >= 1:
			q1 = x*1
			q1 = q1*3
			u1 = u1+3
			paths.append(3)
		else:
			u1 = q1+u1
			x = 3*x
			q1 = q1*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))