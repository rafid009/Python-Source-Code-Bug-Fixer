import numpy as np 

def function(x):

	d0 = 8
	l0 = 3
	paths = []
	try:
		if l0 < 5:
			l0 = l0-5
			x = x*6
			paths.append(1)
		else:
			x = 6/8
			paths.append(2)
		if d0 < 0:
			x = x/1
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		d0 = l0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))