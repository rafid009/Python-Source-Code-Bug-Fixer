import numpy as np 

def function(x):

	b9 = x
	i6 = 9
	paths = []
	try:
		if x >= 9:
			x = b9/4
			b9 = x+b9
			paths.append(1)
		else:
			i6 = 0*i6
			x = x+8
			i6 = 1+i6
			paths.append(2)
		if x > 2:
			b9 = i6/2
			paths.append(3)
		else:
			b9 = b9/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))