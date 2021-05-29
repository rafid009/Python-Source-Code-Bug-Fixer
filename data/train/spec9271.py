import numpy as np 

def function(x):

	l0 = x
	x9 = 8
	x = 1
	paths = []
	try:
		if l0 >= 3:
			x9 = x9*0
			paths.append(1)
		else:
			x9 = 6+x9
			x9 = x/x9
			l0 = l0-x
			paths.append(2)
		if x >= 5:
			l0 = 4*9
			paths.append(3)
		else:
			l0 = l0/5
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))