import numpy as np 

def function(x):

	p1 = x
	d0 = 5
	paths = []
	try:
		if d0 <= 7:
			p1 = 5+1
			d0 = 5+d0
			paths.append(1)
		else:
			p1 = x/p1
			p1 = p1-2
			paths.append(2)
		if x < 0:
			p1 = 9-d0
			x = p1+x
			x = 2+x
			paths.append(3)
		else:
			d0 = 9/d0
			p1 = x+p1
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))