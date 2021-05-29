import numpy as np 

def function(x):

	v8 = x
	f7 = 9
	paths = []
	try:
		if v8 < 8:
			v8 = 2/v8
			x = 7+x
			f7 = x-f7
			paths.append(1)
		else:
			x = 9/x
			paths.append(2)
		if f7 >= 7:
			v8 = f7*v8
			f7 = f7*f7
			paths.append(3)
		else:
			x = v8-7
			v8 = 2*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))