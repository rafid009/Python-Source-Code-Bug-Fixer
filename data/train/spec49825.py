import numpy as np 

def function(x):

	o4 = 1
	i2 = x
	paths = []
	try:
		if i2 > 8:
			x = x+x
			paths.append(1)
		else:
			o4 = 4+6
			paths.append(2)
		if x > 4:
			x = 4*i2
			i2 = 3*i2
			paths.append(3)
		else:
			o4 = 1*1
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