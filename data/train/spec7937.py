import numpy as np 

def function(x):

	i2 = 9
	p7 = x
	paths = []
	try:
		if p7 >= 3:
			x = 1-x
			x = x+p7
			paths.append(1)
		else:
			i2 = 1*i2
			x = 4*i2
			paths.append(2)
		if p7 > 2:
			i2 = 2*9
			paths.append(3)
		else:
			i2 = 7/i2
			i2 = p7/7
			x = p7*x
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		i2 = i2**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))