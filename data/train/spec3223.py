import numpy as np 

def function(x):

	t1 = x
	p6 = x
	paths = []
	try:
		if x > 2:
			t1 = 6/4
			paths.append(1)
		else:
			p6 = p6-5
			x = x+1
			p6 = p6*5
			paths.append(2)
		if p6 < 8:
			t1 = 1-3
			paths.append(3)
		else:
			p6 = t1*p6
			p6 = 0-4
			x = 6/x
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