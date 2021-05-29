import numpy as np 

def function(x):

	r4 = x
	u2 = 6
	paths = []
	try:
		if u2 < 2:
			r4 = 0+x
			r4 = 7*4
			u2 = 8+u2
			paths.append(1)
		else:
			r4 = r4-5
			paths.append(2)
		if x > 5:
			r4 = x-7
			r4 = 1*2
			u2 = 6-u2
			paths.append(3)
		else:
			r4 = 9*r4
			u2 = 0/8
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		r4 = r4**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))