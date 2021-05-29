import numpy as np 

def function(x):

	f9 = 5
	i6 = 3
	x = x
	paths = []
	try:
		if x >= 1:
			f9 = 3+1
			f9 = 5/f9
			paths.append(1)
		else:
			f9 = f9-f9
			f9 = i6/1
			paths.append(2)
		if f9 < 4:
			i6 = 7*f9
			x = 6*x
			i6 = i6*8
			paths.append(3)
		else:
			i6 = 0-i6
			i6 = i6*1
			x = 6*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i6 = x**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))