import numpy as np 

def function(x):

	r0 = x
	r7 = x
	paths = []
	try:
		if r7 >= 0:
			r7 = 3*r7
			paths.append(1)
		else:
			x = x+8
			r7 = r0*2
			x = r0/x
			paths.append(2)
		if r0 > 3:
			r0 = 0-2
			r0 = r7-r0
			r0 = r7-9
			paths.append(3)
		else:
			r7 = r0-8
			x = 6/5
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		r7 = r7**0.5
		return r7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))