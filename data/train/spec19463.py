import numpy as np 

def function(x):

	u2 = 3
	l6 = x
	x = 9
	paths = []
	try:
		if l6 <= 4:
			x = x-6
			x = x*7
			paths.append(1)
		else:
			u2 = u2-3
			paths.append(2)
		if x >= 8:
			x = 1*x
			paths.append(3)
		else:
			l6 = l6/3
			u2 = u2*1
			u2 = 5*u2
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