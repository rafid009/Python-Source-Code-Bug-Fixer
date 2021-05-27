import numpy as np 

def function(x):

	k7 = x
	r3 = x
	paths = []
	try:
		if x < 9:
			k7 = k7/r3
			k7 = k7+1
			paths.append(1)
		else:
			r3 = r3*1
			k7 = k7-k7
			r3 = r3+6
			paths.append(2)
		if r3 <= 4:
			r3 = 7*r3
			k7 = k7+6
			k7 = k7/2
			paths.append(3)
		else:
			k7 = 8+5
			k7 = 9-5
			k7 = 9+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r3 = x**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))