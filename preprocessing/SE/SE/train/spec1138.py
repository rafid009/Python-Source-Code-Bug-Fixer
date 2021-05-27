import numpy as np 

def function(x):

	l1 = x
	q5 = x
	paths = []
	try:
		if l1 > 9:
			l1 = 5*l1
			q5 = q5*q5
			paths.append(1)
		else:
			l1 = q5/x
			paths.append(2)
		if l1 > 0:
			l1 = q5+l1
			l1 = x/4
			paths.append(3)
		else:
			x = x+x
			q5 = q5*8
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