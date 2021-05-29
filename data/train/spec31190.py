import numpy as np 

def function(x):

	t9 = x
	p1 = 4
	paths = []
	try:
		if t9 > 9:
			x = x*9
			t9 = t9+8
			paths.append(1)
		else:
			p1 = p1-4
			p1 = 7+x
			paths.append(2)
		if x <= 3:
			p1 = p1/5
			t9 = t9-8
			paths.append(3)
		else:
			x = 1+p1
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