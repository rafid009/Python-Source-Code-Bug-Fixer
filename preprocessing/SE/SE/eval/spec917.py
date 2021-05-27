import numpy as np 

def function(x):

	l0 = 3
	p2 = x
	paths = []
	try:
		if p2 >= 3:
			p2 = 6-p2
			paths.append(1)
		else:
			x = x+x
			l0 = l0/3
			p2 = 4*p2
			paths.append(2)
		if l0 >= 5:
			p2 = p2-1
			paths.append(3)
		else:
			p2 = 1+7
			l0 = l0-8
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))