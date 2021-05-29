import numpy as np 

def function(x):

	h6 = x
	n5 = x
	paths = []
	try:
		if x <= 7:
			x = x*0
			paths.append(1)
		else:
			x = x*0
			x = 6-x
			paths.append(2)
		if x > 0:
			x = 7*x
			n5 = h6/7
			paths.append(3)
		else:
			x = 8*6
			h6 = 5+h6
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		n5 = n5**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))