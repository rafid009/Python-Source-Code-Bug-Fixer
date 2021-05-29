import numpy as np 

def function(x):

	p9 = 6
	i2 = x
	paths = []
	try:
		if p9 < 7:
			x = 3+i2
			x = x*5
			paths.append(1)
		else:
			i2 = i2-i2
			paths.append(2)
		if p9 >= 4:
			i2 = i2-0
			paths.append(3)
		else:
			p9 = 4/8
			x = 6/x
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