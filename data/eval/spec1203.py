import numpy as np 

def function(x):

	p1 = x
	t0 = 5
	paths = []
	try:
		if x >= 8:
			x = 3-5
			p1 = x-p1
			p1 = 1-p1
			paths.append(1)
		else:
			t0 = 4-t0
			paths.append(2)
		if x <= 9:
			x = p1-6
			p1 = 0-p1
			t0 = x+t0
			paths.append(3)
		else:
			x = x*p1
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