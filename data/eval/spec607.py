import numpy as np 

def function(x):

	v5 = 1
	i2 = x
	paths = []
	try:
		if i2 < 1:
			v5 = v5+x
			i2 = 1+1
			paths.append(1)
		else:
			i2 = 7/2
			v5 = 2-v5
			paths.append(2)
		if v5 > 2:
			v5 = v5+i2
			paths.append(3)
		else:
			i2 = 8*i2
			x = x+8
			v5 = v5+3
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