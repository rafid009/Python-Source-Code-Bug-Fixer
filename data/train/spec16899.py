import numpy as np 

def function(x):

	x8 = x
	v2 = x
	paths = []
	try:
		if v2 > 2:
			x8 = 1+x8
			x8 = x8+3
			x8 = x-v2
			paths.append(1)
		else:
			v2 = 1*v2
			v2 = v2+9
			x8 = 7/3
			paths.append(2)
		if v2 >= 1:
			x8 = 7+x8
			v2 = 0-0
			x8 = x8/4
			paths.append(3)
		else:
			x8 = 8+x8
			v2 = 3+v2
			v2 = 1*v2
			paths.append(4)
		paths.append(5)
		assert v2 >= 0
		v2 = v2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))