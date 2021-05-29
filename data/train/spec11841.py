import numpy as np 

def function(x):

	p9 = 1
	l5 = x
	paths = []
	try:
		if p9 < 3:
			x = 5-x
			paths.append(1)
		else:
			l5 = l5-7
			paths.append(2)
		if p9 < 9:
			x = x-2
			paths.append(3)
		else:
			p9 = p9-p9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))