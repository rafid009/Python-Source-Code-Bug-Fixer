import numpy as np 

def function(x):

	l9 = x
	e7 = x
	x = 1
	paths = []
	try:
		if l9 >= 6:
			l9 = l9+l9
			l9 = 1+e7
			l9 = e7*l9
			paths.append(1)
		else:
			e7 = 6-8
			e7 = 5/6
			paths.append(2)
		if e7 <= 3:
			l9 = l9/x
			e7 = 8/x
			paths.append(3)
		else:
			e7 = e7/9
			e7 = l9+e7
			x = x-x
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