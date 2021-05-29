import numpy as np 

def function(x):

	l5 = 2
	d5 = 9
	paths = []
	try:
		if l5 > 4:
			l5 = l5-l5
			x = x-5
			x = 9*x
			paths.append(1)
		else:
			l5 = l5/2
			l5 = 0/x
			l5 = 5*l5
			paths.append(2)
		if d5 > 0:
			x = 6+x
			l5 = l5+3
			paths.append(3)
		else:
			l5 = l5/6
			d5 = x/l5
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