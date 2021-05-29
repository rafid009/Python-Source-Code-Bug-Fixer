import numpy as np 

def function(x):

	j1 = x
	q2 = x
	paths = []
	try:
		if j1 > 0:
			j1 = 8*q2
			j1 = 6-x
			x = 1-0
			paths.append(1)
		else:
			q2 = 0/q2
			q2 = q2-q2
			j1 = j1-7
			paths.append(2)
		if x < 4:
			j1 = j1-9
			paths.append(3)
		else:
			j1 = j1*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))