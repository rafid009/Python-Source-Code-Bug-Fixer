import numpy as np 

def function(x):

	a9 = 5
	q5 = x
	paths = []
	try:
		if a9 <= 9:
			a9 = a9*4
			q5 = q5/6
			paths.append(1)
		else:
			q5 = 2-x
			paths.append(2)
		if a9 >= 2:
			x = x*q5
			x = x-q5
			a9 = a9*a9
			paths.append(3)
		else:
			q5 = q5-q5
			q5 = x*q5
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