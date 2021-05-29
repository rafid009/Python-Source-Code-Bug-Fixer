import numpy as np 

def function(x):

	r3 = 2
	q8 = x
	paths = []
	try:
		if x < 0:
			r3 = 2+r3
			paths.append(1)
		else:
			r3 = 5+5
			r3 = 9+2
			r3 = r3+5
			paths.append(2)
		if x <= 8:
			r3 = x+r3
			r3 = r3-r3
			paths.append(3)
		else:
			r3 = r3/4
			r3 = 7+q8
			r3 = 3*q8
			paths.append(4)
		paths.append(5)
		assert q8 >= 0
		r3 = q8**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))