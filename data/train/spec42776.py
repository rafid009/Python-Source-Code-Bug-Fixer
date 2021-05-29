import numpy as np 

def function(x):

	i0 = x
	f9 = 8
	x = 7
	paths = []
	try:
		if x > 1:
			i0 = 6/i0
			f9 = 8+f9
			paths.append(1)
		else:
			i0 = i0+6
			paths.append(2)
		if f9 >= 9:
			f9 = f9+x
			paths.append(3)
		else:
			f9 = 5/5
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		f9 = i0**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))