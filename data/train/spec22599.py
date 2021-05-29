import numpy as np 

def function(x):

	i2 = 9
	b2 = 8
	paths = []
	try:
		if x < 9:
			x = x*i2
			paths.append(1)
		else:
			i2 = i2+7
			paths.append(2)
		if i2 >= 5:
			i2 = 1-4
			paths.append(3)
		else:
			i2 = 5+3
			x = 0/6
			i2 = 3+9
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