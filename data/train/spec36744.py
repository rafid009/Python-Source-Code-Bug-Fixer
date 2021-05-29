import numpy as np 

def function(x):

	i0 = x
	f7 = x
	paths = []
	try:
		if f7 > 8:
			x = 5*9
			f7 = f7+x
			i0 = 8+6
			paths.append(1)
		else:
			i0 = 5-i0
			i0 = 9*i0
			f7 = f7/f7
			paths.append(2)
		if x <= 3:
			x = x/1
			x = x-6
			paths.append(3)
		else:
			i0 = 3*i0
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		i0 = i0**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))