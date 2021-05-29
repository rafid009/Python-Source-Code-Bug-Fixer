import numpy as np 

def function(x):

	r1 = 6
	a5 = x
	x = x
	paths = []
	try:
		if x >= 4:
			x = r1*7
			paths.append(1)
		else:
			a5 = a5-9
			r1 = x+x
			paths.append(2)
		if a5 < 7:
			x = 1/x
			paths.append(3)
		else:
			r1 = 8*r1
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		r1 = a5**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))