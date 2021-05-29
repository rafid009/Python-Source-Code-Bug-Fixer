import numpy as np 

def function(x):

	q5 = x
	a0 = 9
	x = 8
	paths = []
	try:
		if x > 6:
			x = x-7
			x = 7+x
			paths.append(1)
		else:
			q5 = x-8
			a0 = 4+a0
			q5 = 8*q5
			paths.append(2)
		if a0 > 2:
			a0 = 2/a0
			a0 = a0/5
			paths.append(3)
		else:
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		a0 = q5**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))