import numpy as np 

def function(x):

	i2 = 7
	p4 = x
	paths = []
	try:
		if x <= 8:
			i2 = 3*5
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if i2 > 4:
			i2 = i2/p4
			paths.append(3)
		else:
			p4 = 9/p4
			p4 = 1-p4
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		x = p4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))