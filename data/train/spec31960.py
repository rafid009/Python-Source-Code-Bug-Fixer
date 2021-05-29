import numpy as np 

def function(x):

	k0 = x
	o1 = 6
	paths = []
	try:
		if k0 <= 9:
			o1 = o1/o1
			o1 = k0*3
			paths.append(1)
		else:
			x = k0/x
			x = 3/x
			paths.append(2)
		if o1 > 5:
			o1 = x*0
			k0 = k0*k0
			x = 5/x
			paths.append(3)
		else:
			o1 = o1/o1
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		k0 = k0**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))