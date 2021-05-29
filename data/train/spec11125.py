import numpy as np 

def function(x):

	u1 = 3
	d3 = 9
	paths = []
	try:
		if x < 4:
			x = x+3
			u1 = u1/u1
			paths.append(1)
		else:
			x = d3*x
			u1 = 4/u1
			d3 = d3+3
			paths.append(2)
		if u1 <= 4:
			u1 = x+9
			paths.append(3)
		else:
			u1 = 0*d3
			u1 = 4-d3
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		u1 = u1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))