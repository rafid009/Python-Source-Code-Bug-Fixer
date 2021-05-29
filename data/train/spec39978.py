import numpy as np 

def function(x):

	q5 = 7
	v5 = x
	paths = []
	try:
		if x > 7:
			q5 = q5/9
			q5 = 1*q5
			paths.append(1)
		else:
			q5 = x-q5
			q5 = 6-q5
			paths.append(2)
		if q5 <= 8:
			x = x/q5
			v5 = 2*v5
			paths.append(3)
		else:
			q5 = q5/x
			v5 = v5+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q5 = x**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))