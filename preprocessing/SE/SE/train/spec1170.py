import numpy as np 

def function(x):

	v8 = 4
	f2 = x
	paths = []
	try:
		if v8 > 1:
			v8 = 3/9
			x = x-f2
			f2 = f2+1
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if f2 <= 9:
			v8 = f2+v8
			paths.append(3)
		else:
			x = x-x
			v8 = 2/v8
			paths.append(4)
		paths.append(5)
		assert f2 >= 0
		v8 = f2**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))