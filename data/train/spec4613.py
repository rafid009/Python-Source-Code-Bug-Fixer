import numpy as np 

def function(x):

	i2 = x
	o2 = x
	paths = []
	try:
		if o2 > 0:
			i2 = 4-i2
			o2 = o2-3
			paths.append(1)
		else:
			x = i2*x
			paths.append(2)
		if x < 0:
			i2 = i2*i2
			o2 = 3+6
			paths.append(3)
		else:
			i2 = i2*2
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))