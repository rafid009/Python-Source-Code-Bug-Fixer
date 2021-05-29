import numpy as np 

def function(x):

	o4 = x
	v3 = x
	paths = []
	try:
		if v3 < 0:
			o4 = x*o4
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if v3 <= 3:
			v3 = 5+8
			o4 = o4+x
			paths.append(3)
		else:
			v3 = o4/v3
			v3 = v3/3
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		v3 = o4**0.5
		return v3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))