import numpy as np 

def function(x):

	r8 = 7
	n9 = 9
	paths = []
	try:
		if r8 < 6:
			x = x*7
			x = x/1
			x = 2+x
			paths.append(1)
		else:
			r8 = 9+r8
			n9 = r8-6
			r8 = r8*n9
			paths.append(2)
		if x <= 6:
			x = 8-n9
			r8 = 6+x
			n9 = n9+2
			paths.append(3)
		else:
			n9 = n9/n9
			x = 0*5
			x = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))