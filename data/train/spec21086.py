import numpy as np 

def function(x):

	q5 = x
	x7 = x
	paths = []
	try:
		if q5 > 3:
			x = x-x
			paths.append(1)
		else:
			q5 = q5*3
			x = x-x7
			q5 = 2+q5
			paths.append(2)
		if x7 > 0:
			q5 = 3-q5
			paths.append(3)
		else:
			q5 = x-q5
			x7 = x/2
			x = x-8
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