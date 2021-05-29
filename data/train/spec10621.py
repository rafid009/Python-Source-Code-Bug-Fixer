import numpy as np 

def function(x):

	r5 = x
	n8 = x
	paths = []
	try:
		if r5 <= 7:
			n8 = r5+n8
			x = x-5
			paths.append(1)
		else:
			n8 = n8-n8
			n8 = 5+n8
			paths.append(2)
		if x >= 8:
			r5 = 9/r5
			n8 = 0*x
			x = x*3
			paths.append(3)
		else:
			n8 = n8-6
			n8 = x+3
			x = r5*x
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		x = r5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))