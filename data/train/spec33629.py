import numpy as np 

def function(x):

	a3 = 7
	l5 = x
	paths = []
	try:
		if x <= 3:
			a3 = a3/5
			paths.append(1)
		else:
			l5 = l5-a3
			l5 = x+a3
			paths.append(2)
		if l5 <= 9:
			x = l5-x
			a3 = 3*l5
			x = 3-l5
			paths.append(3)
		else:
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		l5 = l5**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))