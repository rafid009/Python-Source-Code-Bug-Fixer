import numpy as np 

def function(x):

	d1 = 8
	l7 = x
	paths = []
	try:
		if d1 >= 6:
			d1 = d1/5
			x = 4-x
			paths.append(1)
		else:
			l7 = d1/l7
			d1 = d1-0
			x = x/3
			paths.append(2)
		if l7 < 1:
			x = 5+x
			paths.append(3)
		else:
			d1 = 4/1
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		d1 = l7**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))