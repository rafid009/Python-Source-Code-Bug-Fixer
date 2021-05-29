import numpy as np 

def function(x):

	l4 = x
	d1 = 4
	paths = []
	try:
		if l4 > 0:
			l4 = l4+2
			x = 9+2
			paths.append(1)
		else:
			l4 = 2/l4
			paths.append(2)
		if l4 <= 0:
			l4 = 2*l4
			paths.append(3)
		else:
			d1 = l4/9
			d1 = d1*2
			d1 = d1-0
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		x = l4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))