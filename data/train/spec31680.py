import numpy as np 

def function(x):

	i0 = 6
	b3 = 1
	paths = []
	try:
		if b3 < 4:
			b3 = b3/b3
			i0 = 3/2
			paths.append(1)
		else:
			i0 = i0*9
			b3 = b3*0
			paths.append(2)
		if b3 <= 0:
			x = 2-x
			x = i0/7
			x = x-2
			paths.append(3)
		else:
			i0 = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))