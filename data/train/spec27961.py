import numpy as np 

def function(x):

	v0 = 1
	i2 = x
	paths = []
	try:
		if v0 >= 6:
			i2 = 8/i2
			i2 = v0-i2
			paths.append(1)
		else:
			i2 = 7+i2
			v0 = 0+v0
			i2 = 6*i2
			paths.append(2)
		if x >= 3:
			v0 = i2/4
			i2 = 7-i2
			i2 = x*i2
			paths.append(3)
		else:
			x = 4+x
			x = x/i2
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		v0 = i2**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))