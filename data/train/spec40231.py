import numpy as np 

def function(x):

	i2 = 1
	b0 = x
	paths = []
	try:
		if x > 8:
			i2 = 0+0
			i2 = 7+i2
			paths.append(1)
		else:
			b0 = b0*6
			paths.append(2)
		if x < 1:
			i2 = x-1
			paths.append(3)
		else:
			i2 = i2+1
			b0 = i2*2
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		b0 = i2**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))