import numpy as np 

def function(x):

	l9 = x
	l0 = x
	x = x
	paths = []
	try:
		if x > 7:
			l9 = 4/3
			x = x*x
			x = x+x
			paths.append(1)
		else:
			l0 = 4/l0
			paths.append(2)
		if x <= 2:
			x = x*l0
			x = x*x
			paths.append(3)
		else:
			l9 = l9*x
			x = x-0
			l0 = l0-l9
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		l0 = l9**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))