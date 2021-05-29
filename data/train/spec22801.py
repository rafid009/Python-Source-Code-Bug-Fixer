import numpy as np 

def function(x):

	l3 = 2
	d5 = 2
	paths = []
	try:
		if x > 2:
			l3 = x+l3
			l3 = 1/2
			l3 = 8+4
			paths.append(1)
		else:
			d5 = 7/l3
			x = x*1
			paths.append(2)
		if d5 >= 3:
			d5 = d5*l3
			l3 = l3-3
			paths.append(3)
		else:
			x = 0+x
			l3 = l3+4
			x = d5/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))