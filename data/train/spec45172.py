import numpy as np 

def function(x):

	i6 = x
	l4 = x
	paths = []
	try:
		if l4 > 2:
			x = 5*8
			x = 4/3
			l4 = 2-i6
			paths.append(1)
		else:
			l4 = l4*l4
			l4 = 1/l4
			paths.append(2)
		if l4 <= 4:
			i6 = i6-7
			i6 = l4*6
			paths.append(3)
		else:
			x = x-l4
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