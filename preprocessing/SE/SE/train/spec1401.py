import numpy as np 

def function(x):

	i8 = x
	b5 = 6
	paths = []
	try:
		if i8 > 3:
			x = x-3
			paths.append(1)
		else:
			b5 = 0*b5
			x = b5/4
			paths.append(2)
		if x <= 8:
			b5 = 2+b5
			b5 = 1+3
			paths.append(3)
		else:
			i8 = 8/2
			x = 2-x
			x = x/i8
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		b5 = i8**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))