import numpy as np 

def function(x):

	p1 = 7
	n5 = 1
	x = x
	paths = []
	try:
		if n5 <= 9:
			n5 = 2*x
			x = x*x
			p1 = 5-3
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if x > 5:
			x = x*4
			paths.append(3)
		else:
			n5 = x-9
			n5 = n5-3
			p1 = x*p1
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		p1 = n5**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))