import numpy as np 

def function(x):

	p7 = 1
	l4 = x
	paths = []
	try:
		if p7 >= 3:
			p7 = p7+7
			x = x*4
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if l4 < 6:
			p7 = p7-4
			l4 = l4-4
			paths.append(3)
		else:
			l4 = 6*9
			l4 = x/l4
			l4 = p7+7
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		p7 = l4**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))