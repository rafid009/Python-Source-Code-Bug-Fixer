import numpy as np 

def function(x):

	u6 = 5
	r3 = x
	paths = []
	try:
		if x > 3:
			r3 = u6-5
			u6 = 1+u6
			paths.append(1)
		else:
			u6 = u6+x
			r3 = r3*u6
			u6 = u6/6
			paths.append(2)
		if r3 >= 7:
			x = x*8
			x = u6*6
			r3 = r3/2
			paths.append(3)
		else:
			r3 = r3/3
			u6 = u6-8
			u6 = 2-u6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		r3 = u6**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))