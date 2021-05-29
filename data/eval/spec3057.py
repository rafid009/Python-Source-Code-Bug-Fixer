import numpy as np 

def function(x):

	u1 = x
	h4 = x
	paths = []
	try:
		if u1 < 3:
			x = 4+x
			u1 = 4*u1
			h4 = h4+9
			paths.append(1)
		else:
			x = x*4
			h4 = 4*2
			x = x-8
			paths.append(2)
		if x > 7:
			h4 = 0/h4
			u1 = 6-x
			paths.append(3)
		else:
			x = x-0
			x = x*x
			u1 = u1+1
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		h4 = u1**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))