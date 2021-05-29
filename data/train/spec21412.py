import numpy as np 

def function(x):

	l1 = x
	d5 = 5
	paths = []
	try:
		if l1 > 5:
			d5 = 0*d5
			l1 = l1-8
			paths.append(1)
		else:
			x = 2-3
			l1 = l1/4
			d5 = d5/2
			paths.append(2)
		if d5 <= 7:
			d5 = 6*d5
			d5 = 8*d5
			x = x/2
			paths.append(3)
		else:
			x = d5*x
			x = 5+9
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