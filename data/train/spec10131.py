import numpy as np 

def function(x):

	b3 = 7
	i2 = 3
	paths = []
	try:
		if b3 <= 1:
			b3 = b3*9
			i2 = i2-4
			i2 = 9-i2
			paths.append(1)
		else:
			i2 = b3*b3
			i2 = i2*3
			b3 = b3/b3
			paths.append(2)
		if i2 > 5:
			x = x-x
			x = x-i2
			paths.append(3)
		else:
			i2 = i2+8
			x = x+6
			x = x/3
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