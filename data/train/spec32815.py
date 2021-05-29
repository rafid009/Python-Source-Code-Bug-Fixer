import numpy as np 

def function(x):

	b4 = 8
	i0 = x
	paths = []
	try:
		if i0 > 0:
			x = 6/3
			b4 = 7/8
			paths.append(1)
		else:
			i0 = i0/6
			x = x+9
			paths.append(2)
		if x <= 0:
			b4 = x+9
			b4 = x-b4
			i0 = i0*5
			paths.append(3)
		else:
			i0 = 4+i0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b4 = x**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))