import numpy as np 

def function(x):

	f2 = 9
	y8 = x
	paths = []
	try:
		if f2 <= 0:
			y8 = y8+y8
			f2 = f2-y8
			f2 = f2-y8
			paths.append(1)
		else:
			f2 = 1/x
			f2 = f2/f2
			paths.append(2)
		if y8 < 3:
			x = x/9
			f2 = 0/f2
			x = 8*x
			paths.append(3)
		else:
			x = x+y8
			y8 = y8+1
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		x = y8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))