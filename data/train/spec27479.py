import numpy as np 

def function(x):

	i2 = x
	c1 = 4
	paths = []
	try:
		if x <= 9:
			c1 = x*c1
			i2 = 1*i2
			paths.append(1)
		else:
			c1 = x-c1
			x = x-6
			x = x/1
			paths.append(2)
		if i2 < 1:
			x = x*6
			paths.append(3)
		else:
			c1 = c1+c1
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