import numpy as np 

def function(x):

	p1 = 1
	d4 = x
	paths = []
	try:
		if p1 >= 0:
			d4 = 1*p1
			paths.append(1)
		else:
			x = 5+x
			paths.append(2)
		if d4 < 8:
			p1 = x/p1
			d4 = x/d4
			x = x+6
			paths.append(3)
		else:
			p1 = p1-d4
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		x = p1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))