import numpy as np 

def function(x):

	a0 = x
	q5 = 3
	paths = []
	try:
		if x < 2:
			q5 = q5/a0
			a0 = a0-a0
			paths.append(1)
		else:
			x = q5*x
			q5 = a0+x
			q5 = 3-q5
			paths.append(2)
		if a0 >= 6:
			a0 = q5/a0
			paths.append(3)
		else:
			x = x+6
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		x = q5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))