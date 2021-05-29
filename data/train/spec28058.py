import numpy as np 

def function(x):

	l5 = x
	p2 = x
	paths = []
	try:
		if x > 2:
			p2 = p2-4
			p2 = x-0
			p2 = 1-p2
			paths.append(1)
		else:
			l5 = x/l5
			x = x*7
			paths.append(2)
		if p2 < 3:
			x = 5/x
			x = x/8
			paths.append(3)
		else:
			l5 = l5-p2
			l5 = x-l5
			x = x*1
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