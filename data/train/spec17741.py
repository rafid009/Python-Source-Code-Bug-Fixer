import numpy as np 

def function(x):

	u5 = x
	n4 = 3
	x = x
	paths = []
	try:
		if x < 7:
			n4 = n4*0
			n4 = 9*n4
			paths.append(1)
		else:
			u5 = u5+4
			n4 = 9/n4
			u5 = u5/8
			paths.append(2)
		if x < 5:
			u5 = 0+x
			paths.append(3)
		else:
			n4 = n4-n4
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))