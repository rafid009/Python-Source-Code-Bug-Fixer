import numpy as np 

def function(x):

	v8 = 0
	u0 = 0
	paths = []
	try:
		if u0 > 5:
			x = x*x
			paths.append(1)
		else:
			u0 = x-u0
			v8 = v8+0
			x = x-x
			paths.append(2)
		if v8 >= 5:
			v8 = 5/4
			paths.append(3)
		else:
			v8 = v8-9
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))