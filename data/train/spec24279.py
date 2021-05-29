import numpy as np 

def function(x):

	l5 = x
	u6 = x
	paths = []
	try:
		if l5 >= 9:
			l5 = x+6
			x = 6+u6
			paths.append(1)
		else:
			l5 = l5-8
			paths.append(2)
		if u6 >= 3:
			x = u6+8
			l5 = x+u6
			l5 = 6*l5
			paths.append(3)
		else:
			l5 = u6*u6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))