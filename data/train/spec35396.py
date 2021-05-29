import numpy as np 

def function(x):

	l7 = x
	q4 = x
	paths = []
	try:
		if x > 7:
			q4 = q4+6
			q4 = q4-q4
			x = 3-x
			paths.append(1)
		else:
			q4 = q4*q4
			paths.append(2)
		if l7 > 1:
			l7 = l7*l7
			paths.append(3)
		else:
			q4 = x+2
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		l7 = q4**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))