import numpy as np 

def function(x):

	r1 = x
	r0 = x
	paths = []
	try:
		if r1 < 4:
			r0 = r0/2
			paths.append(1)
		else:
			r0 = 2+r0
			x = 4+1
			r0 = x/x
			paths.append(2)
		if x > 3:
			r0 = 1-r0
			r1 = r1-x
			x = 5+x
			paths.append(3)
		else:
			r1 = r1*r0
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