import numpy as np 

def function(x):

	q2 = 3
	a7 = 1
	paths = []
	try:
		if a7 <= 5:
			a7 = x*a7
			x = x*q2
			x = 4*x
			paths.append(1)
		else:
			x = q2*x
			a7 = a7+q2
			a7 = a7*2
			paths.append(2)
		if x <= 6:
			a7 = a7-8
			q2 = x+q2
			a7 = 3*a7
			paths.append(3)
		else:
			a7 = 2/q2
			x = x-q2
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))