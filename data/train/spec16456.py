import numpy as np 

def function(x):

	l1 = x
	p9 = x
	paths = []
	try:
		if x < 2:
			p9 = l1/1
			l1 = 9*l1
			paths.append(1)
		else:
			l1 = 9/4
			l1 = x*6
			l1 = l1-x
			paths.append(2)
		if l1 > 8:
			x = 0*x
			x = x+x
			p9 = p9+2
			paths.append(3)
		else:
			l1 = p9-4
			l1 = x*4
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		x = l1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))