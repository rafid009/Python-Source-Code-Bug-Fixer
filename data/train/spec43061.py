import numpy as np 

def function(x):

	l1 = 9
	e2 = 8
	paths = []
	try:
		if x > 1:
			x = e2+8
			l1 = l1+4
			l1 = 2-l1
			paths.append(1)
		else:
			l1 = 9*l1
			e2 = 4/x
			l1 = l1+e2
			paths.append(2)
		if l1 <= 2:
			x = x-4
			x = x*9
			paths.append(3)
		else:
			l1 = l1+9
			x = 0*x
			e2 = e2*7
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		e2 = l1**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))