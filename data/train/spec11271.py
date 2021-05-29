import numpy as np 

def function(x):

	v6 = 9
	q5 = x
	x = x
	paths = []
	try:
		if v6 > 6:
			q5 = v6/8
			x = x*7
			q5 = 1/q5
			paths.append(1)
		else:
			q5 = 1/q5
			q5 = x/1
			x = 5-x
			paths.append(2)
		if v6 > 7:
			x = x-0
			q5 = q5*7
			paths.append(3)
		else:
			q5 = 7+q5
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