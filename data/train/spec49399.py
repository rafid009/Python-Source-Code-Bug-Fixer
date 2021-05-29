import numpy as np 

def function(x):

	t1 = 5
	p7 = x
	paths = []
	try:
		if x < 0:
			p7 = 7+2
			p7 = p7+4
			t1 = p7*t1
			paths.append(1)
		else:
			t1 = 4+t1
			paths.append(2)
		if x < 4:
			p7 = 7/p7
			paths.append(3)
		else:
			x = t1+5
			x = 7/t1
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