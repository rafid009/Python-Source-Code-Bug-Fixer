import numpy as np 

def function(x):

	r4 = x
	i6 = x
	paths = []
	try:
		if i6 > 8:
			x = 2/8
			paths.append(1)
		else:
			i6 = 9-7
			r4 = 7+3
			x = 5/x
			paths.append(2)
		if x <= 0:
			i6 = 8+x
			r4 = r4+4
			paths.append(3)
		else:
			r4 = r4+1
			r4 = x-r4
			i6 = i6-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))