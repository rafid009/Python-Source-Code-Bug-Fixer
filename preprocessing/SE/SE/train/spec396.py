import numpy as np 

def function(x):

	f8 = x
	paths = []
	try:
		if x <= 7:
			f8 = f8-7
			paths.append(1)
		else:
			f8 = 9-4
			paths.append(2)
		if x <= 7:
			x = f8+2
			paths.append(3)
		else:
			f8 = f8-0
			f8 = f8-f8
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		f8 = f8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))