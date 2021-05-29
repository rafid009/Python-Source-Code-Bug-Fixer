import numpy as np 

def function(x):

	b8 = 9
	l4 = x
	paths = []
	try:
		if x >= 5:
			b8 = 3-0
			l4 = l4+x
			x = x+9
			paths.append(1)
		else:
			b8 = 8-b8
			l4 = l4*x
			b8 = 6/b8
			paths.append(2)
		if l4 <= 4:
			l4 = x/4
			b8 = x-l4
			x = b8+0
			paths.append(3)
		else:
			b8 = x-b8
			b8 = 2*l4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))