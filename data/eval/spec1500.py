import numpy as np 

def function(x):

	q4 = 2
	l3 = x
	paths = []
	try:
		if q4 <= 0:
			x = 5-x
			x = 0-8
			x = x+4
			paths.append(1)
		else:
			q4 = q4-6
			q4 = 7*2
			paths.append(2)
		if q4 >= 6:
			q4 = 5+6
			q4 = 9/q4
			paths.append(3)
		else:
			l3 = 5/l3
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		q4 = l3**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))