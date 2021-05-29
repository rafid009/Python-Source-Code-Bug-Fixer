import numpy as np 

def function(x):

	l0 = 2
	d2 = 8
	paths = []
	try:
		if x <= 7:
			d2 = 3-1
			paths.append(1)
		else:
			l0 = l0+x
			x = x*d2
			d2 = d2-3
			paths.append(2)
		if l0 >= 2:
			l0 = 0+x
			x = 7-x
			d2 = d2/d2
			paths.append(3)
		else:
			d2 = 9*0
			d2 = d2/8
			x = 0/1
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		d2 = l0**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))