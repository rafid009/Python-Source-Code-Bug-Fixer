import numpy as np 

def function(x):

	i8 = x
	b0 = 6
	paths = []
	try:
		if b0 < 6:
			i8 = 5/1
			paths.append(1)
		else:
			b0 = b0*6
			b0 = x/b0
			b0 = b0-0
			paths.append(2)
		if b0 >= 3:
			i8 = b0-0
			b0 = 4*2
			b0 = b0+7
			paths.append(3)
		else:
			i8 = x+6
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))