import numpy as np 

def function(x):

	q1 = x
	d0 = 3
	paths = []
	try:
		if x < 6:
			d0 = x/7
			d0 = d0+d0
			q1 = 6+q1
			paths.append(1)
		else:
			d0 = 3*d0
			paths.append(2)
		if x >= 3:
			d0 = d0+8
			paths.append(3)
		else:
			q1 = d0/q1
			x = x-q1
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