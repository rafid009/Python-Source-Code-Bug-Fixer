import numpy as np 

def function(x):

	u5 = 6
	v8 = x
	paths = []
	try:
		if u5 >= 2:
			v8 = v8*2
			u5 = 1+0
			paths.append(1)
		else:
			v8 = v8+v8
			paths.append(2)
		if u5 >= 5:
			u5 = 9*v8
			u5 = x-9
			x = 9+x
			paths.append(3)
		else:
			u5 = 6/u5
			u5 = u5/8
			u5 = u5-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))