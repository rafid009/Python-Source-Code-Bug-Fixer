import numpy as np 

def function(x):

	o6 = 0
	i0 = x
	x = 5
	paths = []
	try:
		if i0 <= 7:
			o6 = 4*o6
			paths.append(1)
		else:
			i0 = i0*1
			paths.append(2)
		if i0 < 7:
			o6 = i0/4
			x = 7+x
			paths.append(3)
		else:
			o6 = 1-o6
			x = 0+i0
			i0 = i0-4
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		x = o6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))