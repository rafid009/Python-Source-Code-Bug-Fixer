import numpy as np 

def function(x):

	q1 = 0
	l3 = x
	paths = []
	try:
		if q1 >= 5:
			q1 = 7+q1
			l3 = 3/l3
			paths.append(1)
		else:
			l3 = 5-l3
			x = 9-l3
			l3 = l3-8
			paths.append(2)
		if q1 < 7:
			x = 2/9
			l3 = l3/9
			q1 = 2+3
			paths.append(3)
		else:
			x = 4-x
			l3 = 1+6
			q1 = 1/3
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		l3 = l3**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))