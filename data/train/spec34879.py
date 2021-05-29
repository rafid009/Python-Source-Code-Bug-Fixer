import numpy as np 

def function(x):

	i2 = x
	b3 = 2
	paths = []
	try:
		if i2 <= 2:
			i2 = 4*0
			paths.append(1)
		else:
			i2 = x+i2
			paths.append(2)
		if x >= 7:
			i2 = 0-i2
			b3 = b3*6
			paths.append(3)
		else:
			b3 = 8-6
			x = i2-x
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