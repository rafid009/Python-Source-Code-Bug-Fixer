import numpy as np 

def function(x):

	r8 = x
	k5 = x
	paths = []
	try:
		if x >= 7:
			r8 = 1+0
			k5 = 5-k5
			paths.append(1)
		else:
			r8 = r8-r8
			paths.append(2)
		if x <= 2:
			r8 = 2/x
			x = x*r8
			paths.append(3)
		else:
			k5 = 5-k5
			k5 = x-9
			k5 = k5*4
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		k5 = r8**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))