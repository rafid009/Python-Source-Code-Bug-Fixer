import numpy as np 

def function(x):

	n6 = x
	r0 = 2
	paths = []
	try:
		if r0 > 4:
			n6 = 8-n6
			paths.append(1)
		else:
			n6 = 5*n6
			r0 = x*0
			n6 = 0+n6
			paths.append(2)
		if r0 >= 4:
			n6 = 2/r0
			r0 = 0/8
			paths.append(3)
		else:
			n6 = x+n6
			r0 = r0*r0
			x = 2+0
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		n6 = n6**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))