import numpy as np 

def function(x):

	l2 = 4
	i0 = 5
	paths = []
	try:
		if i0 < 5:
			x = x/8
			i0 = 7+x
			x = x-8
			paths.append(1)
		else:
			i0 = x+9
			i0 = l2-0
			i0 = i0/2
			paths.append(2)
		if l2 >= 3:
			l2 = l2*8
			paths.append(3)
		else:
			i0 = 0-i0
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