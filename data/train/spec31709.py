import numpy as np 

def function(x):

	x6 = 0
	i2 = x
	paths = []
	try:
		if x > 4:
			i2 = 7+i2
			paths.append(1)
		else:
			i2 = i2+5
			i2 = i2*x
			paths.append(2)
		if x6 >= 7:
			i2 = i2+x6
			i2 = i2-2
			i2 = i2*2
			paths.append(3)
		else:
			i2 = i2*8
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