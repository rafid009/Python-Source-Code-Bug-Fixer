import numpy as np 

def function(x):

	x2 = x
	r1 = x
	paths = []
	try:
		if x >= 6:
			x2 = x2*1
			x = 0/x
			r1 = r1*2
			paths.append(1)
		else:
			x = x2-2
			paths.append(2)
		if x >= 5:
			x = r1*5
			x2 = x2*7
			r1 = x+x2
			paths.append(3)
		else:
			r1 = r1/1
			x = x*7
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		r1 = x2**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))