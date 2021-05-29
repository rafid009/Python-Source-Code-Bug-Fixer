import numpy as np 

def function(x):

	v4 = 5
	o9 = 4
	paths = []
	try:
		if x >= 6:
			o9 = x*o9
			v4 = 9+o9
			x = 5+x
			paths.append(1)
		else:
			x = x/x
			v4 = v4+1
			o9 = 6/2
			paths.append(2)
		if v4 < 0:
			v4 = v4+9
			paths.append(3)
		else:
			o9 = o9-6
			o9 = x/o9
			v4 = v4+8
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		v4 = o9**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))