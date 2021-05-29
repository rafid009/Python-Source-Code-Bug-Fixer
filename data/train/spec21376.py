import numpy as np 

def function(x):

	u1 = x
	b1 = 5
	paths = []
	try:
		if b1 >= 2:
			b1 = 2*7
			paths.append(1)
		else:
			u1 = b1*1
			u1 = 9/7
			paths.append(2)
		if b1 < 6:
			b1 = 6-b1
			paths.append(3)
		else:
			x = x*0
			u1 = b1-u1
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