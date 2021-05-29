import numpy as np 

def function(x):

	r8 = x
	k5 = 5
	x = x
	paths = []
	try:
		if x < 1:
			k5 = x-k5
			k5 = 5+9
			paths.append(1)
		else:
			x = 8-x
			paths.append(2)
		if r8 > 4:
			x = x*9
			r8 = r8/6
			paths.append(3)
		else:
			x = x+x
			r8 = r8*7
			k5 = 4*4
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		r8 = r8**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))