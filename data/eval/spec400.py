import numpy as np 

def function(x):

	r4 = 9
	u6 = 4
	paths = []
	try:
		if r4 > 0:
			u6 = u6+x
			x = x*8
			paths.append(1)
		else:
			r4 = 1+r4
			x = u6+x
			x = 3*x
			paths.append(2)
		if x < 1:
			x = 0*x
			r4 = r4-0
			paths.append(3)
		else:
			u6 = u6-8
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		r4 = u6**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))