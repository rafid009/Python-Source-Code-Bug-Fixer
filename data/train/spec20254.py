import numpy as np 

def function(x):

	u1 = x
	d5 = 5
	x = 1
	paths = []
	try:
		if d5 > 0:
			d5 = d5*5
			x = 1+x
			paths.append(1)
		else:
			x = 9/d5
			paths.append(2)
		if x >= 3:
			u1 = 2*7
			paths.append(3)
		else:
			u1 = u1*1
			d5 = 2+d5
			d5 = 1-8
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