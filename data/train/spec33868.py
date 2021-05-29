import numpy as np 

def function(x):

	v3 = x
	r5 = 1
	paths = []
	try:
		if v3 < 9:
			r5 = 9-r5
			paths.append(1)
		else:
			x = x-8
			v3 = v3+1
			r5 = 4+0
			paths.append(2)
		if v3 >= 2:
			v3 = 4+v3
			x = x*v3
			paths.append(3)
		else:
			r5 = v3*r5
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