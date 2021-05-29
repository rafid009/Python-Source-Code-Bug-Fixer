import numpy as np 

def function(x):

	i2 = x
	f1 = 9
	paths = []
	try:
		if f1 > 1:
			f1 = 0-i2
			paths.append(1)
		else:
			x = i2*9
			i2 = 8+x
			x = x/9
			paths.append(2)
		if x > 2:
			x = 2/x
			paths.append(3)
		else:
			f1 = f1*0
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		x = i2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))