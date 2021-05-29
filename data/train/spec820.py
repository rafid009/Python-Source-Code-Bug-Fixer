import numpy as np 

def function(x):

	l6 = x
	k4 = x
	x = 6
	paths = []
	try:
		if k4 <= 9:
			l6 = l6+6
			k4 = k4+7
			x = l6+k4
			paths.append(1)
		else:
			k4 = 6-k4
			x = l6/x
			paths.append(2)
		if l6 >= 6:
			x = x-1
			x = x*3
			l6 = 8*7
			paths.append(3)
		else:
			x = l6*6
			x = x-1
			x = l6*x
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l6 = l6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))