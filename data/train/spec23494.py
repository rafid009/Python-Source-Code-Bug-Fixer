import numpy as np 

def function(x):

	v7 = x
	f4 = 6
	paths = []
	try:
		if x < 1:
			x = x*4
			paths.append(1)
		else:
			f4 = 8-2
			x = x*8
			v7 = 1/v7
			paths.append(2)
		if f4 >= 1:
			f4 = f4-5
			f4 = x/7
			x = 2+f4
			paths.append(3)
		else:
			f4 = f4+f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))