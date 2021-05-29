import numpy as np 

def function(x):

	e2 = 5
	l7 = 1
	paths = []
	try:
		if e2 < 2:
			x = 0/2
			paths.append(1)
		else:
			e2 = e2+4
			paths.append(2)
		if x < 0:
			l7 = x/3
			x = x*0
			e2 = e2-l7
			paths.append(3)
		else:
			x = 2+e2
			e2 = e2+1
			x = x-1
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))