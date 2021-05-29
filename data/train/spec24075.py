import numpy as np 

def function(x):

	l6 = x
	q9 = x
	paths = []
	try:
		if q9 > 6:
			q9 = 0+5
			paths.append(1)
		else:
			q9 = 5-l6
			l6 = l6/5
			x = x-x
			paths.append(2)
		if q9 <= 3:
			x = x-3
			l6 = 7*l6
			paths.append(3)
		else:
			l6 = l6-x
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		l6 = q9**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))