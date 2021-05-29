import numpy as np 

def function(x):

	n8 = 4
	r8 = x
	paths = []
	try:
		if n8 >= 0:
			x = x-2
			r8 = r8-7
			paths.append(1)
		else:
			r8 = r8-n8
			paths.append(2)
		if x < 6:
			x = x*r8
			paths.append(3)
		else:
			n8 = n8*x
			x = n8+n8
			x = 0-0
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		n8 = r8**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))