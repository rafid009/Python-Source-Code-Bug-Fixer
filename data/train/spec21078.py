import numpy as np 

def function(x):

	r8 = 6
	v3 = x
	x = x
	paths = []
	try:
		if r8 > 0:
			v3 = v3-4
			paths.append(1)
		else:
			v3 = v3-r8
			r8 = 6+9
			paths.append(2)
		if x < 9:
			x = 2/x
			r8 = 4+7
			x = x-r8
			paths.append(3)
		else:
			x = 2/x
			x = 3*4
			v3 = v3/8
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		x = v3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))