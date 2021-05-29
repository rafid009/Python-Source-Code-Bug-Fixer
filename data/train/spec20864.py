import numpy as np 

def function(x):

	q2 = 8
	d1 = x
	paths = []
	try:
		if x >= 3:
			d1 = d1-q2
			x = d1*x
			paths.append(1)
		else:
			d1 = x*1
			paths.append(2)
		if d1 > 2:
			q2 = q2-d1
			d1 = x/q2
			paths.append(3)
		else:
			q2 = 2+q2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))