import numpy as np 

def function(x):

	v8 = x
	u0 = 7
	paths = []
	try:
		if u0 <= 2:
			x = v8-x
			v8 = u0*v8
			paths.append(1)
		else:
			x = x*3
			v8 = v8+8
			paths.append(2)
		if v8 >= 9:
			v8 = u0*v8
			paths.append(3)
		else:
			v8 = v8+8
			v8 = 1-6
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