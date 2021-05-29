import numpy as np 

def function(x):

	d1 = 1
	l5 = 3
	paths = []
	try:
		if l5 > 7:
			x = x/d1
			l5 = l5-5
			l5 = 5-l5
			paths.append(1)
		else:
			d1 = 6*d1
			paths.append(2)
		if l5 > 5:
			l5 = 2*x
			d1 = 9/d1
			l5 = l5/2
			paths.append(3)
		else:
			d1 = x+8
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))