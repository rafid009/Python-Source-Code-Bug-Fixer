import numpy as np 

def function(x):

	b4 = 0
	q5 = x
	paths = []
	try:
		if x >= 6:
			q5 = 0-5
			b4 = b4-x
			b4 = 5/5
			paths.append(1)
		else:
			q5 = 5+q5
			q5 = 6-q5
			b4 = b4/7
			paths.append(2)
		if x > 0:
			b4 = 9-b4
			paths.append(3)
		else:
			x = 1*q5
			q5 = 2/q5
			q5 = q5-b4
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