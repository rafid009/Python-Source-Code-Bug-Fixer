import numpy as np 

def function(x):

	o0 = x
	u1 = 4
	paths = []
	try:
		if u1 >= 4:
			x = 2-8
			x = x-x
			paths.append(1)
		else:
			x = 1*8
			u1 = u1/1
			paths.append(2)
		if o0 > 4:
			o0 = 0+8
			u1 = 0/u1
			u1 = x+3
			paths.append(3)
		else:
			u1 = x-2
			u1 = x+u1
			u1 = u1*7
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		o0 = u1**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))