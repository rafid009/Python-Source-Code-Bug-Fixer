import numpy as np 

def function(x):

	i8 = 6
	r1 = x
	paths = []
	try:
		if x < 6:
			r1 = 7*r1
			i8 = 0-i8
			paths.append(1)
		else:
			i8 = 9+i8
			i8 = 3*i8
			r1 = 7-r1
			paths.append(2)
		if i8 > 7:
			r1 = r1-9
			paths.append(3)
		else:
			i8 = i8/x
			i8 = r1*i8
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