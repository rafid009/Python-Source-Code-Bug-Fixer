import numpy as np 

def function(x):

	i8 = 4
	r1 = 0
	x = 4
	paths = []
	try:
		if i8 > 6:
			r1 = 9/4
			paths.append(1)
		else:
			r1 = i8-5
			r1 = r1/6
			i8 = i8/6
			paths.append(2)
		if i8 >= 2:
			x = 1-x
			x = x*r1
			x = 2-2
			paths.append(3)
		else:
			i8 = i8-6
			x = r1/x
			i8 = i8-2
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		x = r1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))