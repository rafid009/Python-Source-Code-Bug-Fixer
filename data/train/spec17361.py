import numpy as np 

def function(x):

	x7 = 4
	r8 = x
	paths = []
	try:
		if x > 7:
			x7 = r8+3
			r8 = r8*3
			r8 = 6/x7
			paths.append(1)
		else:
			x = 9+x
			x = x-x
			paths.append(2)
		if r8 < 0:
			x = x*7
			x7 = x7/x7
			paths.append(3)
		else:
			x = x-3
			r8 = r8+9
			r8 = r8*r8
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x7 = r8**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))