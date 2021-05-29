import numpy as np 

def function(x):

	l1 = 2
	g9 = 0
	paths = []
	try:
		if g9 > 7:
			g9 = 0-g9
			l1 = l1-1
			paths.append(1)
		else:
			l1 = x/9
			g9 = 6*g9
			g9 = g9-l1
			paths.append(2)
		if l1 >= 2:
			x = x*l1
			l1 = 3+g9
			l1 = l1*6
			paths.append(3)
		else:
			x = x+8
			g9 = 2-g9
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