import numpy as np 

def function(x):

	i2 = x
	k6 = 6
	paths = []
	try:
		if k6 >= 6:
			i2 = 4*i2
			x = 8/7
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if i2 > 5:
			i2 = 0+i2
			paths.append(3)
		else:
			x = x+9
			x = 7/2
			x = x+9
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		k6 = i2**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))