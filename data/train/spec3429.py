import numpy as np 

def function(x):

	i2 = x
	o7 = x
	paths = []
	try:
		if o7 > 2:
			i2 = 2+i2
			paths.append(1)
		else:
			o7 = x*2
			x = x-3
			paths.append(2)
		if x < 0:
			x = o7-3
			x = x+i2
			o7 = 0/6
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		o7 = i2**0.5
		return o7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))