import numpy as np 

def function(x):

	l6 = 8
	b2 = 6
	paths = []
	try:
		if b2 > 0:
			b2 = x/b2
			l6 = l6/l6
			paths.append(1)
		else:
			x = 2/3
			paths.append(2)
		if l6 >= 4:
			x = 9/8
			l6 = 8-l6
			l6 = l6-9
			paths.append(3)
		else:
			x = x*9
			l6 = l6-b2
			l6 = 3*l6
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l6 = l6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))