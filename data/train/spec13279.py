import numpy as np 

def function(x):

	n3 = x
	i2 = 2
	paths = []
	try:
		if x > 0:
			x = 8/x
			i2 = 9/6
			paths.append(1)
		else:
			i2 = i2-6
			x = i2/n3
			x = x-4
			paths.append(2)
		if x > 9:
			x = 6+x
			n3 = 9*n3
			n3 = n3-2
			paths.append(3)
		else:
			i2 = x+9
			n3 = n3+x
			i2 = 6-x
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		n3 = i2**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))