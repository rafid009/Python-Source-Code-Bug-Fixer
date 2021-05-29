import numpy as np 

def function(x):

	t3 = x
	q7 = 7
	paths = []
	try:
		if t3 > 6:
			x = q7*x
			q7 = 1+q7
			x = t3+x
			paths.append(1)
		else:
			q7 = q7/4
			x = x-2
			x = x-7
			paths.append(2)
		if x < 7:
			t3 = q7-7
			paths.append(3)
		else:
			q7 = q7+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q7 = x**0.5
		return q7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))