import numpy as np 

def function(x):

	v7 = 8
	b1 = 5
	paths = []
	try:
		if b1 > 3:
			x = 7+x
			v7 = 0/2
			b1 = 3/7
			paths.append(1)
		else:
			b1 = 2+v7
			x = 7+x
			paths.append(2)
		if b1 >= 8:
			x = 4+4
			paths.append(3)
		else:
			v7 = v7+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b1 = x**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))