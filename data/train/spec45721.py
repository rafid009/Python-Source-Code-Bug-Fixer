import numpy as np 

def function(x):

	i2 = 2
	v8 = x
	paths = []
	try:
		if v8 < 2:
			x = x+0
			i2 = x/3
			paths.append(1)
		else:
			v8 = 7-v8
			x = v8/8
			i2 = i2/i2
			paths.append(2)
		if v8 >= 4:
			v8 = v8-v8
			paths.append(3)
		else:
			x = 7+x
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