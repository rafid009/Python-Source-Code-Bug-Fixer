import numpy as np 

def function(x):

	i2 = x
	r1 = 3
	paths = []
	try:
		if i2 > 6:
			i2 = i2*1
			x = 9*x
			i2 = 7/i2
			paths.append(1)
		else:
			x = x/3
			i2 = x+i2
			paths.append(2)
		if x <= 9:
			x = i2*7
			i2 = i2-r1
			paths.append(3)
		else:
			x = 9+x
			x = 0*i2
			i2 = 2-i2
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