import numpy as np 

def function(x):

	p9 = x
	i2 = 0
	paths = []
	try:
		if x >= 8:
			i2 = p9-i2
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if i2 > 8:
			i2 = i2-8
			i2 = i2-3
			paths.append(3)
		else:
			p9 = x/3
			p9 = i2*9
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