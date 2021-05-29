import numpy as np 

def function(x):

	q9 = 2
	i1 = 7
	paths = []
	try:
		if x >= 2:
			i1 = 7*3
			i1 = i1-0
			q9 = 5*q9
			paths.append(1)
		else:
			q9 = x-q9
			paths.append(2)
		if x >= 0:
			i1 = i1*6
			i1 = 4+5
			x = x*x
			paths.append(3)
		else:
			q9 = i1*i1
			x = x+x
			q9 = q9*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))