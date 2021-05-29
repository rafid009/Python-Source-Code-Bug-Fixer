import numpy as np 

def function(x):

	i2 = x
	k2 = 4
	paths = []
	try:
		if i2 <= 0:
			i2 = k2/x
			paths.append(1)
		else:
			x = 4/7
			k2 = k2-5
			x = x+1
			paths.append(2)
		if x <= 8:
			i2 = 0*i2
			i2 = 7/k2
			paths.append(3)
		else:
			k2 = k2-9
			i2 = i2-x
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