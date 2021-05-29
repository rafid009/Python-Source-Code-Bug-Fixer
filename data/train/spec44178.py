import numpy as np 

def function(x):

	p7 = 7
	b6 = x
	paths = []
	try:
		if x >= 3:
			p7 = p7*p7
			p7 = 9-p7
			paths.append(1)
		else:
			x = 5*0
			p7 = p7/b6
			paths.append(2)
		if x >= 1:
			p7 = p7+x
			b6 = p7+x
			paths.append(3)
		else:
			x = 6-p7
			b6 = b6*7
			x = b6-x
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