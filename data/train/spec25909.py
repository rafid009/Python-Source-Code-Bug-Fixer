import numpy as np 

def function(x):

	o2 = x
	k5 = 1
	paths = []
	try:
		if o2 < 4:
			x = 4*0
			x = x+4
			x = 3/6
			paths.append(1)
		else:
			x = 6/1
			paths.append(2)
		if k5 <= 3:
			x = x*x
			paths.append(3)
		else:
			o2 = x+8
			o2 = k5/2
			k5 = k5-9
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		x = o2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))