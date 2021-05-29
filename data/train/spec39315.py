import numpy as np 

def function(x):

	q9 = x
	y4 = x
	paths = []
	try:
		if q9 < 1:
			y4 = y4+q9
			q9 = 5+q9
			paths.append(1)
		else:
			x = x/5
			y4 = y4*6
			paths.append(2)
		if x > 1:
			q9 = x-8
			paths.append(3)
		else:
			x = x+q9
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