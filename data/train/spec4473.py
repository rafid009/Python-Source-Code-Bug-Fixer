import numpy as np 

def function(x):

	l6 = x
	u7 = x
	paths = []
	try:
		if u7 > 6:
			x = 9/2
			u7 = u7*l6
			paths.append(1)
		else:
			u7 = 3/u7
			paths.append(2)
		if l6 <= 0:
			l6 = 8-l6
			u7 = 2*u7
			l6 = 1*l6
			paths.append(3)
		else:
			l6 = l6-7
			x = 4/x
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