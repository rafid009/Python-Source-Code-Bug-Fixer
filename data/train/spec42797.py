import numpy as np 

def function(x):

	u5 = x
	n1 = 4
	paths = []
	try:
		if u5 < 8:
			x = x+2
			x = x*x
			n1 = n1+n1
			paths.append(1)
		else:
			x = x/6
			x = 0/x
			x = 6-x
			paths.append(2)
		if n1 > 6:
			x = 4/x
			u5 = u5-1
			paths.append(3)
		else:
			n1 = n1-7
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		n1 = u5**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))