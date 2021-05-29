import numpy as np 

def function(x):

	p0 = x
	l1 = 4
	paths = []
	try:
		if x >= 8:
			l1 = x+l1
			l1 = l1/x
			paths.append(1)
		else:
			l1 = 5+x
			p0 = p0/1
			paths.append(2)
		if l1 > 0:
			x = 2-5
			l1 = 5-x
			p0 = 0/p0
			paths.append(3)
		else:
			x = x*0
			l1 = x/4
			x = x-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))