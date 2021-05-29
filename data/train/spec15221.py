import numpy as np 

def function(x):

	r0 = x
	n3 = 6
	paths = []
	try:
		if r0 <= 5:
			x = x+x
			r0 = r0+1
			paths.append(1)
		else:
			x = 1+n3
			n3 = n3*n3
			paths.append(2)
		if n3 > 5:
			x = x/n3
			r0 = 5-r0
			n3 = 5*9
			paths.append(3)
		else:
			n3 = 0/n3
			x = 7/x
			r0 = 0+n3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))