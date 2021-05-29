import numpy as np 

def function(x):

	e3 = x
	l5 = x
	paths = []
	try:
		if l5 < 2:
			l5 = l5/x
			l5 = 7-8
			e3 = 4*l5
			paths.append(1)
		else:
			e3 = e3*2
			x = 0-2
			x = l5/1
			paths.append(2)
		if e3 > 5:
			x = x-8
			paths.append(3)
		else:
			l5 = 5*l5
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