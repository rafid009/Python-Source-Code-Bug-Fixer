import numpy as np 

def function(x):

	b2 = 4
	i2 = 0
	paths = []
	try:
		if x >= 5:
			b2 = b2+4
			b2 = x-x
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if b2 < 7:
			b2 = 3/x
			b2 = i2-8
			i2 = i2+i2
			paths.append(3)
		else:
			i2 = 9/2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		i2 = b2**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))