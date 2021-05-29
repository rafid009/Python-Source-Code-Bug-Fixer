import numpy as np 

def function(x):

	k0 = x
	o1 = 3
	x = x
	paths = []
	try:
		if x < 4:
			k0 = x*o1
			o1 = o1*4
			paths.append(1)
		else:
			o1 = k0/9
			paths.append(2)
		if k0 >= 3:
			o1 = k0*o1
			x = 4-8
			paths.append(3)
		else:
			o1 = o1+0
			k0 = 3+k0
			k0 = k0+5
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x = k0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))