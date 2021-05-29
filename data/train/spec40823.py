import numpy as np 

def function(x):

	j1 = 7
	l2 = 0
	paths = []
	try:
		if x < 0:
			j1 = 2/j1
			j1 = j1*3
			paths.append(1)
		else:
			j1 = j1*x
			j1 = 1/j1
			x = x*4
			paths.append(2)
		if l2 <= 7:
			j1 = j1*5
			l2 = l2-j1
			x = 1/x
			paths.append(3)
		else:
			x = l2-8
			l2 = l2-2
			j1 = j1*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))