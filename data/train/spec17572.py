import numpy as np 

def function(x):

	r3 = x
	n9 = x
	paths = []
	try:
		if r3 >= 2:
			x = x*3
			paths.append(1)
		else:
			x = 4*x
			x = n9/x
			r3 = r3-2
			paths.append(2)
		if x < 3:
			r3 = 7*r3
			paths.append(3)
		else:
			n9 = n9/7
			r3 = 1-7
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		r3 = n9**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))