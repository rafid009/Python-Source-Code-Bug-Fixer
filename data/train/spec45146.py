import numpy as np 

def function(x):

	l7 = 5
	p9 = 5
	paths = []
	try:
		if p9 > 1:
			x = l7+x
			p9 = p9*6
			paths.append(1)
		else:
			p9 = 9/3
			x = x-6
			paths.append(2)
		if l7 <= 6:
			p9 = p9*6
			paths.append(3)
		else:
			p9 = l7*p9
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