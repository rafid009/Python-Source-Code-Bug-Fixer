import numpy as np 

def function(x):

	n0 = x
	q4 = x
	paths = []
	try:
		if x <= 8:
			n0 = x*n0
			q4 = q4+3
			q4 = x-1
			paths.append(1)
		else:
			q4 = q4*0
			q4 = n0-4
			x = 1+4
			paths.append(2)
		if n0 < 4:
			x = x/n0
			paths.append(3)
		else:
			x = x+x
			q4 = q4/6
			n0 = n0*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))