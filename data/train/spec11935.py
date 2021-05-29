import numpy as np 

def function(x):

	d9 = x
	p1 = 6
	paths = []
	try:
		if p1 >= 3:
			d9 = 0/9
			d9 = 9/p1
			paths.append(1)
		else:
			x = x/4
			x = 4*x
			x = p1-9
			paths.append(2)
		if d9 <= 7:
			d9 = 4-d9
			d9 = d9*4
			x = 0-5
			paths.append(3)
		else:
			x = 9+3
			p1 = p1+p1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))