import numpy as np 

def function(x):

	r5 = 2
	n3 = x
	paths = []
	try:
		if n3 > 1:
			r5 = r5+1
			paths.append(1)
		else:
			n3 = 7+n3
			paths.append(2)
		if x >= 9:
			x = 8/n3
			paths.append(3)
		else:
			r5 = r5-6
			n3 = n3*2
			r5 = 5-r5
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		r5 = n3**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))