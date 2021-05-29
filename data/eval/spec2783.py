import numpy as np 

def function(x):

	q5 = x
	j9 = 0
	paths = []
	try:
		if j9 > 0:
			q5 = q5*4
			j9 = 3/j9
			q5 = 8*q5
			paths.append(1)
		else:
			j9 = 1+j9
			paths.append(2)
		if x <= 2:
			j9 = 5/j9
			j9 = j9*5
			q5 = x/x
			paths.append(3)
		else:
			q5 = q5*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))