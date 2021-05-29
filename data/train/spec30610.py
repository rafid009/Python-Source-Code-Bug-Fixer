import numpy as np 

def function(x):

	u6 = 7
	v0 = x
	paths = []
	try:
		if x <= 4:
			v0 = v0+x
			u6 = 6-7
			paths.append(1)
		else:
			x = x+4
			v0 = 1-v0
			paths.append(2)
		if x > 8:
			v0 = 1*v0
			v0 = v0/2
			x = 1-x
			paths.append(3)
		else:
			x = u6-1
			v0 = u6/5
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		v0 = u6**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))