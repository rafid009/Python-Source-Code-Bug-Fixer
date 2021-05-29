import numpy as np 

def function(x):

	k0 = 3
	f1 = 8
	paths = []
	try:
		if x < 1:
			k0 = x*k0
			f1 = f1+k0
			paths.append(1)
		else:
			f1 = k0+f1
			x = x-3
			x = 3*0
			paths.append(2)
		if x < 6:
			f1 = 6-f1
			paths.append(3)
		else:
			k0 = 2*k0
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		f1 = k0**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))