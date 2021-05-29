import numpy as np 

def function(x):

	r8 = 9
	r0 = x
	paths = []
	try:
		if r0 < 7:
			x = 7+3
			x = 2+x
			x = 2/x
			paths.append(1)
		else:
			r0 = r0+r0
			x = x-0
			r8 = r8+2
			paths.append(2)
		if r8 <= 0:
			r8 = r8-1
			r8 = 7+r8
			paths.append(3)
		else:
			r0 = r0+x
			x = 6-x
			r8 = 1-r8
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		r8 = r0**0.5
		return r8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))