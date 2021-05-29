import numpy as np 

def function(x):

	q9 = 9
	l6 = 4
	paths = []
	try:
		if l6 >= 6:
			l6 = l6-6
			paths.append(1)
		else:
			x = x/2
			l6 = l6+7
			paths.append(2)
		if l6 > 3:
			q9 = 2/q9
			l6 = 2-l6
			paths.append(3)
		else:
			l6 = l6-7
			q9 = 8-q9
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		q9 = l6**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))