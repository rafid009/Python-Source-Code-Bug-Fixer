import numpy as np 

def function(x):

	v8 = 6
	f4 = 2
	paths = []
	try:
		if v8 > 7:
			f4 = 4+f4
			x = 6*x
			v8 = v8*v8
			paths.append(1)
		else:
			v8 = 4-f4
			paths.append(2)
		if x >= 4:
			f4 = 7*f4
			x = f4-x
			v8 = v8-f4
			paths.append(3)
		else:
			f4 = x*8
			x = 3*f4
			x = v8/1
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))