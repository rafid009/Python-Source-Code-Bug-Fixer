import numpy as np 

def function(x):

	j9 = 6
	p4 = x
	paths = []
	try:
		if x < 2:
			x = x*x
			p4 = p4-8
			paths.append(1)
		else:
			x = 3*x
			p4 = x+p4
			x = 2+x
			paths.append(2)
		if p4 >= 8:
			x = 2+x
			p4 = 5+p4
			x = x-6
			paths.append(3)
		else:
			p4 = x+p4
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		x = p4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))