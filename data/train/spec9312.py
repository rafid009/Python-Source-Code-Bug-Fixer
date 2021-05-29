import numpy as np 

def function(x):

	j9 = 9
	i2 = x
	paths = []
	try:
		if x <= 4:
			x = x/j9
			j9 = 8+x
			paths.append(1)
		else:
			x = 6*x
			paths.append(2)
		if i2 >= 8:
			i2 = 5-i2
			j9 = 4/j9
			j9 = 5-8
			paths.append(3)
		else:
			j9 = 6*8
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