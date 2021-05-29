import numpy as np 

def function(x):

	q8 = 7
	i2 = x
	paths = []
	try:
		if x <= 8:
			i2 = i2+6
			i2 = 9+0
			i2 = i2*3
			paths.append(1)
		else:
			i2 = i2/q8
			paths.append(2)
		if x > 5:
			i2 = x-i2
			paths.append(3)
		else:
			q8 = 6+0
			q8 = q8+5
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		x = i2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))