import numpy as np 

def function(x):

	r8 = x
	u6 = 2
	paths = []
	try:
		if r8 > 5:
			u6 = x*2
			x = x*3
			x = 4*x
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if x < 6:
			u6 = u6-4
			r8 = u6+9
			r8 = r8+u6
			paths.append(3)
		else:
			r8 = 5*6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))