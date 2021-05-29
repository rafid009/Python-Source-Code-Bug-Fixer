import numpy as np 

def function(x):

	l4 = 3
	a0 = 1
	paths = []
	try:
		if a0 <= 2:
			l4 = l4/l4
			x = 1*x
			x = x/9
			paths.append(1)
		else:
			x = 3+x
			paths.append(2)
		if x > 9:
			l4 = a0+0
			l4 = l4-7
			l4 = 4*l4
			paths.append(3)
		else:
			a0 = 1*l4
			l4 = x+x
			x = 8-5
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))