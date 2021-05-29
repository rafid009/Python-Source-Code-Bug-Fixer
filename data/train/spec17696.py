import numpy as np 

def function(x):

	n2 = x
	q6 = 4
	paths = []
	try:
		if x > 1:
			n2 = n2-5
			paths.append(1)
		else:
			q6 = 3*3
			n2 = n2*n2
			x = x*5
			paths.append(2)
		if q6 <= 8:
			n2 = q6/9
			x = 6-x
			paths.append(3)
		else:
			x = x*5
			n2 = x/8
			n2 = x-7
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		x = n2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))