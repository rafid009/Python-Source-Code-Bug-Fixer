import numpy as np 

def function(x):

	q5 = 2
	l8 = x
	paths = []
	try:
		if x <= 1:
			q5 = 2/q5
			paths.append(1)
		else:
			l8 = q5*q5
			l8 = l8+1
			q5 = q5/x
			paths.append(2)
		if l8 > 5:
			q5 = 9-q5
			q5 = 1*q5
			x = x-l8
			paths.append(3)
		else:
			q5 = 8-3
			q5 = q5-7
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		x = l8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))