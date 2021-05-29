import numpy as np 

def function(x):

	r0 = x
	i2 = x
	paths = []
	try:
		if i2 >= 2:
			r0 = r0+1
			paths.append(1)
		else:
			i2 = i2+5
			i2 = 3+x
			r0 = r0/x
			paths.append(2)
		if x >= 5:
			r0 = 9/r0
			paths.append(3)
		else:
			x = 4-x
			i2 = i2-0
			i2 = x/i2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))