import numpy as np 

def function(x):

	r0 = 3
	v8 = 6
	paths = []
	try:
		if x >= 4:
			v8 = 6+v8
			paths.append(1)
		else:
			r0 = r0+x
			r0 = 2+r0
			paths.append(2)
		if r0 > 8:
			x = 1+v8
			v8 = v8+9
			v8 = v8+4
			paths.append(3)
		else:
			x = 9+0
			x = 0-2
			r0 = 3/r0
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		x = r0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))