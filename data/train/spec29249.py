import numpy as np 

def function(x):

	r1 = 3
	r4 = x
	paths = []
	try:
		if r1 < 9:
			r1 = 8*x
			paths.append(1)
		else:
			r4 = 5-7
			x = x/8
			r1 = r1*8
			paths.append(2)
		if r4 <= 6:
			x = x*r4
			paths.append(3)
		else:
			x = x*x
			x = x/4
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))