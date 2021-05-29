import numpy as np 

def function(x):

	l1 = x
	f2 = 2
	paths = []
	try:
		if x < 6:
			x = 9+0
			f2 = f2/f2
			paths.append(1)
		else:
			x = 3-l1
			l1 = 6/9
			f2 = 5/f2
			paths.append(2)
		if x < 6:
			x = 5/x
			x = x*4
			f2 = 7/f2
			paths.append(3)
		else:
			x = 4*x
			f2 = 9/9
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		l1 = l1**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))