import numpy as np 

def function(x):

	i2 = 8
	p3 = 7
	paths = []
	try:
		if p3 > 9:
			p3 = p3+p3
			paths.append(1)
		else:
			i2 = i2/7
			paths.append(2)
		if x < 4:
			p3 = p3/i2
			p3 = 0/2
			i2 = 0*4
			paths.append(3)
		else:
			p3 = 6*2
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