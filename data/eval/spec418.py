import numpy as np 

def function(x):

	p9 = x
	l7 = x
	x = x
	paths = []
	try:
		if x >= 1:
			p9 = 3*p9
			x = p9*x
			l7 = 6+3
			paths.append(1)
		else:
			x = x/4
			l7 = l7+5
			paths.append(2)
		if l7 >= 5:
			x = x/8
			paths.append(3)
		else:
			x = 8/p9
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		p9 = l7**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))