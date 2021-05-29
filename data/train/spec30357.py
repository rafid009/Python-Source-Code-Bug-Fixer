import numpy as np 

def function(x):

	i6 = 2
	b3 = x
	x = 1
	paths = []
	try:
		if i6 >= 0:
			i6 = 0+8
			paths.append(1)
		else:
			b3 = 0-b3
			b3 = x+i6
			b3 = 8/b3
			paths.append(2)
		if x <= 0:
			b3 = 8/3
			b3 = 5+b3
			x = x+x
			paths.append(3)
		else:
			b3 = b3*5
			i6 = 9/6
			b3 = b3*8
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		i6 = b3**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))