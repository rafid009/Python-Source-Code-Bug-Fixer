import numpy as np 

def function(x):

	b0 = 9
	o2 = x
	paths = []
	try:
		if x > 2:
			o2 = 1+2
			paths.append(1)
		else:
			b0 = b0*o2
			x = b0*o2
			o2 = 1+7
			paths.append(2)
		if b0 < 4:
			x = x*1
			b0 = b0/1
			x = 3*8
			paths.append(3)
		else:
			x = 4+9
			b0 = b0-0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		o2 = b0**0.5
		return o2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))