import numpy as np 

def function(x):

	k1 = 8
	q3 = 6
	paths = []
	try:
		if k1 < 4:
			q3 = q3-k1
			k1 = k1-q3
			paths.append(1)
		else:
			q3 = x*3
			k1 = 7-8
			q3 = 8/q3
			paths.append(2)
		if q3 >= 9:
			q3 = 1*k1
			q3 = k1/2
			q3 = q3-k1
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		q3 = k1**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))