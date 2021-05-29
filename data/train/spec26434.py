import numpy as np 

def function(x):

	p7 = x
	l3 = x
	paths = []
	try:
		if x >= 0:
			l3 = l3*9
			x = p7*p7
			paths.append(1)
		else:
			p7 = l3*2
			l3 = 6+3
			paths.append(2)
		if x >= 8:
			l3 = l3+x
			l3 = l3*6
			paths.append(3)
		else:
			x = 4/x
			p7 = x-9
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