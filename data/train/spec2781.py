import numpy as np 

def function(x):

	q6 = x
	t7 = 0
	paths = []
	try:
		if t7 < 1:
			q6 = q6/7
			paths.append(1)
		else:
			x = x-0
			paths.append(2)
		if x >= 8:
			t7 = q6+2
			q6 = q6-q6
			t7 = 6*t7
			paths.append(3)
		else:
			t7 = 0-x
			x = 9+x
			t7 = 4/q6
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