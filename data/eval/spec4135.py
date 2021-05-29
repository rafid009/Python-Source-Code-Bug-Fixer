import numpy as np 

def function(x):

	r6 = 8
	q6 = 5
	x = x
	paths = []
	try:
		if r6 < 7:
			q6 = 3/3
			q6 = q6-1
			q6 = 3-q6
			paths.append(1)
		else:
			r6 = r6*6
			r6 = 8*7
			paths.append(2)
		if x > 9:
			q6 = 3-2
			q6 = 7-q6
			paths.append(3)
		else:
			r6 = x/r6
			x = x-q6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		q6 = r6**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))