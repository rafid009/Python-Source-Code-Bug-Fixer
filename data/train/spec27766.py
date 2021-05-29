import numpy as np 

def function(x):

	t9 = 9
	q6 = 6
	paths = []
	try:
		if x <= 1:
			x = x+x
			paths.append(1)
		else:
			x = 2+7
			paths.append(2)
		if t9 > 8:
			t9 = t9+t9
			paths.append(3)
		else:
			q6 = q6/q6
			q6 = 1+q6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))