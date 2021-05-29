import numpy as np 

def function(x):

	p4 = 1
	c0 = x
	paths = []
	try:
		if p4 < 9:
			p4 = 6*p4
			paths.append(1)
		else:
			x = x*2
			paths.append(2)
		if p4 >= 6:
			p4 = c0/c0
			x = c0+c0
			x = x-c0
			paths.append(3)
		else:
			p4 = 5-0
			paths.append(4)
		paths.append(5)
		assert c0 >= 0
		x = c0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))