import numpy as np 

def function(x):

	r9 = x
	r0 = 6
	paths = []
	try:
		if x > 3:
			x = r9*r0
			x = 0/1
			x = 8+5
			paths.append(1)
		else:
			r0 = 0*r0
			x = 8/x
			paths.append(2)
		if r9 < 4:
			x = x/9
			paths.append(3)
		else:
			r0 = r0/4
			r9 = 7-r9
			x = x/6
			paths.append(4)
		paths.append(5)
		assert r9 >= 0
		r0 = r9**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))