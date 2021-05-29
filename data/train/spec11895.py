import numpy as np 

def function(x):

	t2 = x
	r4 = 7
	paths = []
	try:
		if t2 < 5:
			r4 = 0+t2
			r4 = r4-5
			paths.append(1)
		else:
			x = x/8
			paths.append(2)
		if r4 > 7:
			r4 = 6+r4
			paths.append(3)
		else:
			x = x*r4
			x = x*6
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