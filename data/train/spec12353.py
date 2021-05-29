import numpy as np 

def function(x):

	f4 = x
	v8 = 9
	x = 9
	paths = []
	try:
		if x <= 5:
			v8 = 4*v8
			x = x+0
			paths.append(1)
		else:
			v8 = 8-5
			x = f4-x
			f4 = f4-4
			paths.append(2)
		if v8 < 1:
			x = x+8
			paths.append(3)
		else:
			x = v8-f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		v8 = f4**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))