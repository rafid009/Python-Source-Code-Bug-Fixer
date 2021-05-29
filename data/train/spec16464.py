import numpy as np 

def function(x):

	n3 = 4
	x6 = 5
	x = x
	paths = []
	try:
		if x >= 5:
			n3 = n3+6
			n3 = n3*4
			paths.append(1)
		else:
			x6 = 6/x6
			x = x6+x
			x6 = x6*1
			paths.append(2)
		if x6 < 2:
			x6 = 4+x6
			paths.append(3)
		else:
			x = x/x6
			n3 = 6-8
			x6 = x6+9
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		n3 = n3**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))