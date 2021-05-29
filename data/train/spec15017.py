import numpy as np 

def function(x):

	q5 = 3
	x8 = x
	paths = []
	try:
		if q5 <= 1:
			q5 = 1/8
			q5 = x8*9
			paths.append(1)
		else:
			q5 = x8+q5
			x = x/q5
			x8 = x8*2
			paths.append(2)
		if x8 <= 3:
			q5 = 7-q5
			q5 = 0/8
			paths.append(3)
		else:
			x8 = x8-x8
			x8 = x8-9
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