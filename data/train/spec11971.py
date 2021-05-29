import numpy as np 

def function(x):

	i1 = x
	n5 = x
	paths = []
	try:
		if n5 < 3:
			n5 = 0/5
			x = x*i1
			paths.append(1)
		else:
			n5 = n5*8
			i1 = 1+5
			n5 = 6/4
			paths.append(2)
		if x < 4:
			n5 = 0*n5
			i1 = i1+1
			n5 = 5/i1
			paths.append(3)
		else:
			n5 = n5+6
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