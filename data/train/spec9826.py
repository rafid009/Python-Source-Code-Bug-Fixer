import numpy as np 

def function(x):

	i8 = 0
	r9 = x
	paths = []
	try:
		if i8 < 0:
			i8 = i8+i8
			paths.append(1)
		else:
			r9 = r9+x
			paths.append(2)
		if r9 > 9:
			i8 = i8-7
			paths.append(3)
		else:
			x = x+i8
			i8 = r9*i8
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r9 = r9**0.5
		return r9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))