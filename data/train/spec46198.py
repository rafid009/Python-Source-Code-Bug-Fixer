import numpy as np 

def function(x):

	k7 = x
	r8 = 3
	paths = []
	try:
		if r8 >= 1:
			r8 = 5+r8
			paths.append(1)
		else:
			k7 = r8/k7
			x = x/3
			x = x/8
			paths.append(2)
		if r8 >= 1:
			x = x/2
			r8 = k7/r8
			k7 = 5/5
			paths.append(3)
		else:
			k7 = k7-r8
			r8 = 2*r8
			k7 = k7*6
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		x = r8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))