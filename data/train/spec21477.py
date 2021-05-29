import numpy as np 

def function(x):

	q7 = 9
	t6 = x
	paths = []
	try:
		if x < 5:
			x = x*5
			x = 1*x
			paths.append(1)
		else:
			q7 = 6-q7
			paths.append(2)
		if t6 >= 8:
			t6 = t6*q7
			x = 9+x
			q7 = 5/q7
			paths.append(3)
		else:
			q7 = 7-6
			x = x-8
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		q7 = t6**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))