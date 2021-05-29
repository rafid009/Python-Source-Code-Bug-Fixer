import numpy as np 

def function(x):

	b5 = x
	i7 = x
	paths = []
	try:
		if i7 > 3:
			x = x-3
			x = i7+0
			b5 = 8+x
			paths.append(1)
		else:
			x = 8/1
			paths.append(2)
		if i7 >= 3:
			x = 4+x
			x = b5-6
			paths.append(3)
		else:
			x = 5-9
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))