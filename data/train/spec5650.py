import numpy as np 

def function(x):

	i7 = 2
	f4 = 5
	paths = []
	try:
		if f4 >= 4:
			f4 = f4-8
			i7 = i7/4
			paths.append(1)
		else:
			x = 3+x
			f4 = f4*3
			paths.append(2)
		if f4 < 1:
			f4 = x-f4
			i7 = i7-x
			i7 = 8-i7
			paths.append(3)
		else:
			i7 = i7/8
			i7 = i7*3
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		f4 = i7**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))