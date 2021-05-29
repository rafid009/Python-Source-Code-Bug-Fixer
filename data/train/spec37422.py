import numpy as np 

def function(x):

	i0 = x
	b7 = x
	paths = []
	try:
		if b7 <= 7:
			b7 = 5/i0
			i0 = i0+x
			b7 = b7/9
			paths.append(1)
		else:
			x = x-i0
			i0 = 3+i0
			x = 9-x
			paths.append(2)
		if x <= 7:
			x = x/6
			paths.append(3)
		else:
			i0 = 7*i0
			i0 = i0*9
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