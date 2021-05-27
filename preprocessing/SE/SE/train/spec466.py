import numpy as np 

def function(x):

	l1 = x
	d6 = 3
	paths = []
	try:
		if l1 < 1:
			d6 = d6-6
			l1 = l1*l1
			l1 = l1/x
			paths.append(1)
		else:
			l1 = l1+x
			paths.append(2)
		if l1 >= 2:
			d6 = d6+x
			x = 6/7
			paths.append(3)
		else:
			l1 = l1/4
			l1 = 9/l1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))