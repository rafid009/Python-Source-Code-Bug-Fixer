import numpy as np 

def function(x):

	i2 = 8
	x6 = 9
	x = x
	paths = []
	try:
		if x6 < 8:
			x6 = 5*0
			i2 = x6/i2
			i2 = x/8
			paths.append(1)
		else:
			x6 = x/x6
			i2 = i2-7
			paths.append(2)
		if i2 >= 5:
			x = i2*4
			paths.append(3)
		else:
			x = 5*x
			i2 = i2-5
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))