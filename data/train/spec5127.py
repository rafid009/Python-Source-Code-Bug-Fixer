import numpy as np 

def function(x):

	x8 = 1
	q5 = x
	paths = []
	try:
		if x8 < 1:
			q5 = 7*q5
			paths.append(1)
		else:
			x = x/x
			q5 = 3/q5
			paths.append(2)
		if x >= 2:
			x = x*3
			q5 = 9-q5
			paths.append(3)
		else:
			q5 = 9/q5
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x8 = q5**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))