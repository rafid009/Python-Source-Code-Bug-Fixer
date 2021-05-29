import numpy as np 

def function(x):

	r4 = 4
	u4 = 6
	x = 1
	paths = []
	try:
		if r4 >= 8:
			r4 = 7*r4
			paths.append(1)
		else:
			u4 = u4/x
			r4 = r4*x
			r4 = r4*2
			paths.append(2)
		if u4 <= 4:
			u4 = 1+8
			x = 0*2
			paths.append(3)
		else:
			u4 = 1-u4
			x = 3+x
			x = x*2
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x = u4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))