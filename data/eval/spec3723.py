import numpy as np 

def function(x):

	x1 = x
	u1 = 5
	paths = []
	try:
		if x <= 5:
			x1 = u1*5
			paths.append(1)
		else:
			x = x+8
			x1 = x1+u1
			paths.append(2)
		if u1 > 4:
			x = x+0
			u1 = x*8
			u1 = x-u1
			paths.append(3)
		else:
			x = x*2
			x = 0/u1
			x1 = x1-x1
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		x1 = u1**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))