import numpy as np 

def function(x):

	d5 = 5
	q1 = x
	paths = []
	try:
		if x >= 8:
			d5 = 3/d5
			paths.append(1)
		else:
			d5 = d5/1
			d5 = d5+q1
			paths.append(2)
		if d5 < 5:
			x = 1*x
			x = x-q1
			paths.append(3)
		else:
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		q1 = q1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))