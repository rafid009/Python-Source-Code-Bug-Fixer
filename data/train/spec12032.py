import numpy as np 

def function(x):

	l7 = 1
	j1 = x
	paths = []
	try:
		if x > 3:
			l7 = x/l7
			paths.append(1)
		else:
			l7 = 5*l7
			paths.append(2)
		if x < 8:
			x = x-1
			paths.append(3)
		else:
			j1 = 3*j1
			j1 = j1*x
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		j1 = j1**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))