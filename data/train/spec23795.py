import numpy as np 

def function(x):

	i2 = 3
	p0 = 5
	paths = []
	try:
		if i2 < 1:
			i2 = i2+i2
			p0 = p0+i2
			paths.append(1)
		else:
			p0 = 2+0
			paths.append(2)
		if i2 > 3:
			x = x*i2
			x = 4*p0
			x = i2-2
			paths.append(3)
		else:
			p0 = 2-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i2 = x**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))