import numpy as np 

def function(x):

	l5 = 5
	a8 = x
	paths = []
	try:
		if l5 < 3:
			l5 = l5+0
			a8 = a8-a8
			paths.append(1)
		else:
			l5 = l5*l5
			x = 3/x
			paths.append(2)
		if a8 < 1:
			x = 4+x
			l5 = 0*4
			x = x+0
			paths.append(3)
		else:
			a8 = a8-6
			l5 = l5/l5
			l5 = a8/1
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