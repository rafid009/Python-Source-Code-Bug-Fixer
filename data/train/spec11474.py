import numpy as np 

def function(x):

	q1 = 0
	v9 = x
	x = x
	paths = []
	try:
		if x <= 8:
			q1 = q1-5
			v9 = v9+0
			v9 = 1*v9
			paths.append(1)
		else:
			q1 = x-q1
			paths.append(2)
		if x >= 8:
			q1 = q1-0
			v9 = v9+8
			paths.append(3)
		else:
			x = q1+x
			v9 = 2*1
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