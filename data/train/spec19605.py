import numpy as np 

def function(x):

	n1 = x
	u0 = 2
	paths = []
	try:
		if x <= 8:
			n1 = n1-5
			n1 = n1*3
			x = x/6
			paths.append(1)
		else:
			n1 = n1+4
			paths.append(2)
		if n1 <= 5:
			n1 = n1*1
			paths.append(3)
		else:
			u0 = u0-6
			n1 = n1+3
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		u0 = n1**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))