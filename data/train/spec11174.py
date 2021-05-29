import numpy as np 

def function(x):

	i2 = 9
	o6 = 7
	paths = []
	try:
		if x <= 1:
			x = o6/o6
			i2 = i2-8
			o6 = x-x
			paths.append(1)
		else:
			o6 = i2+i2
			paths.append(2)
		if x > 1:
			o6 = i2-o6
			x = 6-x
			paths.append(3)
		else:
			o6 = i2*3
			x = i2+1
			o6 = 1+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i2 = x**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))