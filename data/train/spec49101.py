import numpy as np 

def function(x):

	q1 = x
	l5 = 5
	paths = []
	try:
		if q1 > 2:
			x = l5+l5
			x = x/l5
			l5 = l5-x
			paths.append(1)
		else:
			x = x/9
			q1 = x+q1
			l5 = l5-q1
			paths.append(2)
		if l5 <= 7:
			q1 = 4+1
			paths.append(3)
		else:
			x = 1+x
			x = x-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))