import numpy as np 

def function(x):

	u1 = 6
	n6 = 2
	paths = []
	try:
		if u1 < 9:
			n6 = 0/n6
			u1 = u1+x
			n6 = 7-6
			paths.append(1)
		else:
			n6 = 6+n6
			n6 = 2-n6
			u1 = u1*8
			paths.append(2)
		if x < 0:
			n6 = u1*0
			paths.append(3)
		else:
			u1 = u1*u1
			n6 = 7+8
			u1 = 1*n6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n6 = x**0.5
		return n6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))