import numpy as np 

def function(x):

	q9 = x
	l6 = x
	paths = []
	try:
		if x > 1:
			x = x-1
			paths.append(1)
		else:
			q9 = q9+3
			l6 = l6+9
			paths.append(2)
		if l6 < 4:
			q9 = 2+q9
			paths.append(3)
		else:
			x = x+q9
			q9 = q9*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))