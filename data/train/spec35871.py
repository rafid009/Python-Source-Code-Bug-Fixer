import numpy as np 

def function(x):

	u1 = x
	r6 = 4
	paths = []
	try:
		if r6 < 6:
			x = x-r6
			r6 = r6/r6
			paths.append(1)
		else:
			r6 = 9/8
			x = x+6
			x = x*5
			paths.append(2)
		if u1 > 3:
			r6 = r6+6
			u1 = u1-4
			paths.append(3)
		else:
			u1 = 6+3
			x = u1*3
			u1 = u1-7
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		r6 = u1**0.5
		return r6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))