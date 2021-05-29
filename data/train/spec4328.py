import numpy as np 

def function(x):

	l2 = x
	u6 = 9
	paths = []
	try:
		if x > 6:
			x = 5-x
			paths.append(1)
		else:
			x = x*9
			u6 = x/1
			x = x*x
			paths.append(2)
		if l2 > 5:
			u6 = 3*9
			paths.append(3)
		else:
			u6 = u6+u6
			x = x+5
			l2 = x-l2
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