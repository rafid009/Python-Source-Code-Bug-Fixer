import numpy as np 

def function(x):

	l9 = x
	a5 = x
	paths = []
	try:
		if l9 < 1:
			a5 = x-5
			l9 = x/a5
			paths.append(1)
		else:
			l9 = l9/5
			l9 = 9-3
			paths.append(2)
		if x > 4:
			l9 = 2/7
			paths.append(3)
		else:
			x = a5*x
			a5 = x+a5
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		l9 = l9**0.5
		return l9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))