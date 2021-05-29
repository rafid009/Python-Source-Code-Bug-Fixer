import numpy as np 

def function(x):

	n4 = x
	u1 = x
	paths = []
	try:
		if x > 9:
			n4 = n4*u1
			n4 = n4-x
			n4 = 5/n4
			paths.append(1)
		else:
			u1 = n4/u1
			u1 = 4+u1
			u1 = u1-6
			paths.append(2)
		if u1 >= 4:
			x = x+x
			paths.append(3)
		else:
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert n4 >= 0
		n4 = n4**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))