import numpy as np 

def function(x):

	q1 = x
	l8 = 9
	paths = []
	try:
		if q1 > 3:
			l8 = q1/l8
			q1 = 8*q1
			paths.append(1)
		else:
			q1 = q1*6
			q1 = x+x
			paths.append(2)
		if q1 <= 9:
			l8 = 1+5
			l8 = 9*0
			paths.append(3)
		else:
			x = x+0
			x = x*x
			x = x-q1
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		l8 = q1**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))