import numpy as np 

def function(x):

	i6 = x
	f8 = 9
	paths = []
	try:
		if i6 <= 1:
			i6 = x-1
			x = x/f8
			i6 = i6+6
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if i6 > 7:
			f8 = i6/f8
			f8 = 6+f8
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))