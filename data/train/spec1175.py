import numpy as np 

def function(x):

	x6 = x
	u1 = x
	paths = []
	try:
		if u1 < 8:
			u1 = 0*u1
			x = 6/9
			paths.append(1)
		else:
			x6 = x6-0
			u1 = u1/2
			x6 = x6-x
			paths.append(2)
		if x >= 0:
			u1 = x6*4
			paths.append(3)
		else:
			x6 = x*0
			x6 = 4*8
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		x6 = u1**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))