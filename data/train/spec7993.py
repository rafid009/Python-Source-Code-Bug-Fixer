import numpy as np 

def function(x):

	l6 = x
	j1 = 0
	paths = []
	try:
		if x < 4:
			j1 = j1*1
			j1 = j1/l6
			paths.append(1)
		else:
			j1 = j1-l6
			x = x*j1
			l6 = 6*l6
			paths.append(2)
		if j1 <= 6:
			j1 = 9*7
			l6 = 7+l6
			paths.append(3)
		else:
			j1 = l6*9
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))