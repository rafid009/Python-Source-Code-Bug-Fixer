import numpy as np 

def function(x):

	t6 = 1
	q7 = x
	paths = []
	try:
		if x > 5:
			q7 = 2/q7
			q7 = q7-6
			t6 = 9*4
			paths.append(1)
		else:
			x = x/q7
			q7 = q7-x
			paths.append(2)
		if t6 > 5:
			q7 = 0-x
			x = x*t6
			paths.append(3)
		else:
			x = x+t6
			q7 = 4/9
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		q7 = q7**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))