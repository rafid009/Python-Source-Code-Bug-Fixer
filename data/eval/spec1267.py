import numpy as np 

def function(x):

	i5 = 1
	b1 = 9
	paths = []
	try:
		if b1 < 9:
			b1 = b1-x
			paths.append(1)
		else:
			b1 = 3-b1
			paths.append(2)
		if i5 >= 8:
			i5 = x+i5
			x = 8+x
			paths.append(3)
		else:
			i5 = 0+i5
			x = x/b1
			i5 = i5+i5
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		x = b1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))