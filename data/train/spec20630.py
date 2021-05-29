import numpy as np 

def function(x):

	i7 = 6
	i2 = x
	paths = []
	try:
		if i2 > 3:
			i2 = 4+5
			i7 = i7+i7
			i7 = x+0
			paths.append(1)
		else:
			x = 4*x
			paths.append(2)
		if i2 < 0:
			i2 = 6*i2
			i7 = i7/i2
			i2 = i2-4
			paths.append(3)
		else:
			i2 = i7*i2
			x = x/8
			x = x/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i7 = x**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))