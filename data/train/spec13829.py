import numpy as np 

def function(x):

	f0 = x
	q3 = 7
	x = 6
	paths = []
	try:
		if x > 7:
			q3 = q3+7
			x = f0+q3
			paths.append(1)
		else:
			q3 = x/x
			q3 = q3/q3
			q3 = q3-5
			paths.append(2)
		if x >= 0:
			x = x-x
			paths.append(3)
		else:
			x = 3*x
			q3 = q3+q3
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		q3 = f0**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))