import numpy as np 

def function(x):

	l9 = x
	p7 = x
	paths = []
	try:
		if l9 > 2:
			p7 = 3+4
			paths.append(1)
		else:
			l9 = l9+4
			p7 = 6-3
			paths.append(2)
		if p7 < 9:
			p7 = x-4
			paths.append(3)
		else:
			l9 = 3/l9
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		p7 = l9**0.5
		return p7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))