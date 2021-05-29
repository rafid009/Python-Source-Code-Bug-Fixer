import numpy as np 

def function(x):

	i2 = 3
	f8 = x
	x = 2
	paths = []
	try:
		if i2 <= 9:
			i2 = 9-i2
			paths.append(1)
		else:
			x = 5*x
			f8 = f8-4
			paths.append(2)
		if i2 > 3:
			f8 = f8+8
			i2 = 3-i2
			paths.append(3)
		else:
			x = x*1
			x = x+1
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		f8 = i2**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))