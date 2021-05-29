import numpy as np 

def function(x):

	n5 = x
	u9 = x
	paths = []
	try:
		if x < 9:
			u9 = 5*u9
			paths.append(1)
		else:
			n5 = n5-u9
			u9 = 2+u9
			paths.append(2)
		if x < 4:
			n5 = 5*8
			n5 = 1*3
			u9 = 4+u9
			paths.append(3)
		else:
			x = x+u9
			u9 = x+4
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		n5 = u9**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))