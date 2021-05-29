import numpy as np 

def function(x):

	v6 = 6
	q2 = 0
	paths = []
	try:
		if x < 1:
			v6 = 0-x
			v6 = v6/5
			v6 = v6/v6
			paths.append(1)
		else:
			v6 = 1*4
			x = 2-x
			x = 2+1
			paths.append(2)
		if v6 < 8:
			q2 = 5-5
			paths.append(3)
		else:
			q2 = 9/5
			v6 = v6-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))