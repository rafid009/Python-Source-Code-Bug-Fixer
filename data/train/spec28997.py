import numpy as np 

def function(x):

	v8 = x
	r8 = x
	x = x
	paths = []
	try:
		if v8 >= 2:
			v8 = v8-v8
			paths.append(1)
		else:
			r8 = r8-r8
			paths.append(2)
		if v8 < 1:
			r8 = r8-6
			paths.append(3)
		else:
			x = r8*0
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))