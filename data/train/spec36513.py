import numpy as np 

def function(x):

	u0 = x
	b0 = 5
	paths = []
	try:
		if u0 >= 2:
			x = x-x
			paths.append(1)
		else:
			x = b0/5
			b0 = x-b0
			x = x/1
			paths.append(2)
		if b0 > 7:
			u0 = u0*0
			paths.append(3)
		else:
			x = x*8
			x = x*0
			x = u0*6
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		u0 = b0**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))