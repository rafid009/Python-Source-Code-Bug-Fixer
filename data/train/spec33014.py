import numpy as np 

def function(x):

	r8 = 9
	n5 = 5
	paths = []
	try:
		if x >= 5:
			n5 = n5-x
			paths.append(1)
		else:
			r8 = 0+n5
			paths.append(2)
		if r8 <= 7:
			x = r8*x
			paths.append(3)
		else:
			r8 = r8+6
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		r8 = n5**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))