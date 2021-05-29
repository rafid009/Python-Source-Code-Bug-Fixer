import numpy as np 

def function(x):

	t4 = 3
	p4 = x
	paths = []
	try:
		if x > 2:
			x = 7*x
			p4 = p4*1
			paths.append(1)
		else:
			p4 = p4/t4
			paths.append(2)
		if p4 < 6:
			t4 = 9+8
			t4 = 2/8
			x = 2/p4
			paths.append(3)
		else:
			t4 = t4/7
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