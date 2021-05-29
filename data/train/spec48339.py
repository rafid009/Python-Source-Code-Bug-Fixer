import numpy as np 

def function(x):

	r6 = x
	n5 = 1
	x = 8
	paths = []
	try:
		if x >= 1:
			n5 = 7+n5
			paths.append(1)
		else:
			r6 = 1-r6
			r6 = r6/8
			paths.append(2)
		if x <= 8:
			x = x+1
			n5 = 5/n5
			paths.append(3)
		else:
			x = 4/r6
			n5 = 2*2
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		n5 = r6**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))