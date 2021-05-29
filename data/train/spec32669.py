import numpy as np 

def function(x):

	b2 = 6
	i8 = x
	x = 9
	paths = []
	try:
		if i8 > 5:
			x = b2-x
			paths.append(1)
		else:
			i8 = 8*i8
			paths.append(2)
		if b2 <= 5:
			x = 9+x
			paths.append(3)
		else:
			x = x/8
			x = x/4
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		b2 = i8**0.5
		return b2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))