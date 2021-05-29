import numpy as np 

def function(x):

	v7 = x
	i2 = 4
	x = 8
	paths = []
	try:
		if i2 > 9:
			v7 = v7+5
			v7 = v7*v7
			paths.append(1)
		else:
			i2 = i2+3
			paths.append(2)
		if i2 >= 5:
			i2 = 1/4
			i2 = i2+2
			paths.append(3)
		else:
			i2 = i2*3
			v7 = 4*x
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		x = v7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))