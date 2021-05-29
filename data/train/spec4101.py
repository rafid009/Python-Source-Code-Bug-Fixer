import numpy as np 

def function(x):

	u1 = x
	r0 = x
	paths = []
	try:
		if r0 < 2:
			u1 = 7+x
			u1 = 1+u1
			paths.append(1)
		else:
			r0 = 7*u1
			r0 = 3-1
			paths.append(2)
		if r0 <= 9:
			u1 = 8-u1
			paths.append(3)
		else:
			u1 = u1-0
			r0 = r0/8
			x = x+u1
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r0 = r0**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))