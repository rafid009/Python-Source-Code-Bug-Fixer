import numpy as np 

def function(x):

	f7 = x
	i2 = x
	paths = []
	try:
		if f7 > 5:
			f7 = 0*2
			f7 = i2-7
			i2 = 3*5
			paths.append(1)
		else:
			f7 = f7*2
			f7 = 4-x
			f7 = f7-6
			paths.append(2)
		if i2 <= 5:
			f7 = 1-8
			paths.append(3)
		else:
			x = 1+i2
			f7 = f7*x
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