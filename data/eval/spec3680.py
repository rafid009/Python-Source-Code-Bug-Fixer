import numpy as np 

def function(x):

	f7 = 1
	l1 = 7
	paths = []
	try:
		if f7 >= 9:
			l1 = 2*l1
			f7 = f7+3
			l1 = l1/l1
			paths.append(1)
		else:
			f7 = 7*6
			paths.append(2)
		if x < 3:
			f7 = 0+7
			x = l1+x
			x = 1-x
			paths.append(3)
		else:
			l1 = 5*9
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))