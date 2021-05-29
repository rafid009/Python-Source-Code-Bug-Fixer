import numpy as np 

def function(x):

	r1 = x
	x2 = x
	x = 5
	paths = []
	try:
		if x <= 4:
			x = x/r1
			x = x*3
			r1 = x+9
			paths.append(1)
		else:
			r1 = r1*2
			x2 = 6*x2
			x2 = x2-5
			paths.append(2)
		if x2 < 7:
			r1 = r1/4
			paths.append(3)
		else:
			x2 = x-1
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