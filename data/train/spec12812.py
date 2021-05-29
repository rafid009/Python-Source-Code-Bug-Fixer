import numpy as np 

def function(x):

	b7 = 7
	q9 = x
	x = x
	paths = []
	try:
		if x >= 9:
			b7 = b7*x
			b7 = b7/q9
			paths.append(1)
		else:
			q9 = q9+q9
			b7 = b7/8
			b7 = b7-b7
			paths.append(2)
		if b7 >= 1:
			x = 7*q9
			paths.append(3)
		else:
			x = 5+b7
			b7 = b7/5
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q9 = q9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))