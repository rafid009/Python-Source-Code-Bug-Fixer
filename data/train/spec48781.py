import numpy as np 

def function(x):

	f0 = x
	i8 = 3
	paths = []
	try:
		if i8 <= 3:
			x = f0-i8
			i8 = i8-2
			f0 = f0/7
			paths.append(1)
		else:
			f0 = 1-7
			paths.append(2)
		if i8 < 9:
			i8 = f0-i8
			f0 = i8/9
			x = 4+x
			paths.append(3)
		else:
			i8 = 4-9
			x = 2*5
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))