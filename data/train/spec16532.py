import numpy as np 

def function(x):

	n2 = 7
	x6 = 9
	paths = []
	try:
		if x >= 9:
			x = x/3
			x6 = 4+x6
			paths.append(1)
		else:
			x6 = x6+x6
			n2 = 5*x
			n2 = 7/n2
			paths.append(2)
		if n2 < 1:
			x6 = x6+x6
			x6 = x/9
			paths.append(3)
		else:
			x = x+x
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