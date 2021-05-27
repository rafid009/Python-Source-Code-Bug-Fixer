import numpy as np 

def function(x):

	n0 = x
	b6 = 8
	paths = []
	try:
		if x < 1:
			x = 8/x
			x = 8*x
			paths.append(1)
		else:
			b6 = b6+x
			n0 = 3-4
			b6 = x*4
			paths.append(2)
		if x <= 5:
			x = n0*0
			n0 = n0+2
			b6 = b6-b6
			paths.append(3)
		else:
			x = 3/5
			n0 = n0/8
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		n0 = n0**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))