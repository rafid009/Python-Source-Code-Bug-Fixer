import numpy as np 

def function(x):

	p2 = x
	t3 = 5
	x = x
	paths = []
	try:
		if p2 >= 1:
			x = x+3
			x = 0-5
			p2 = p2*x
			paths.append(1)
		else:
			p2 = 5-p2
			p2 = 3/p2
			paths.append(2)
		if t3 > 6:
			p2 = t3/p2
			t3 = t3*9
			paths.append(3)
		else:
			t3 = t3*p2
			x = x-t3
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