import numpy as np 

def function(x):

	l6 = x
	k4 = x
	paths = []
	try:
		if k4 >= 2:
			l6 = l6+2
			x = 0*x
			x = x+1
			paths.append(1)
		else:
			x = 7/x
			x = 7*5
			l6 = x-l6
			paths.append(2)
		if k4 >= 2:
			k4 = k4/3
			l6 = x/l6
			x = x-1
			paths.append(3)
		else:
			l6 = l6-8
			l6 = l6*8
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		l6 = k4**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))