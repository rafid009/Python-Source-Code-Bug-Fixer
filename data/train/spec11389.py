import numpy as np 

def function(x):

	t2 = x
	q5 = x
	x = x
	paths = []
	try:
		if q5 >= 3:
			t2 = 1*t2
			q5 = q5*6
			paths.append(1)
		else:
			x = x/x
			q5 = q5-2
			paths.append(2)
		if t2 > 8:
			x = 6*x
			x = q5/x
			q5 = t2*q5
			paths.append(3)
		else:
			q5 = 2-q5
			x = q5-3
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))