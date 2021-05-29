import numpy as np 

def function(x):

	u2 = 9
	q6 = x
	paths = []
	try:
		if x < 8:
			u2 = u2-8
			x = u2*x
			x = x-2
			paths.append(1)
		else:
			q6 = x+4
			q6 = 8-x
			paths.append(2)
		if u2 <= 0:
			q6 = x+q6
			paths.append(3)
		else:
			q6 = q6-5
			paths.append(4)
		paths.append(5)
		assert q6 >= 0
		q6 = q6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))