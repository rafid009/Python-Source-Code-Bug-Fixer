import numpy as np 

def function(x):

	f6 = 7
	k0 = 0
	paths = []
	try:
		if k0 < 9:
			f6 = f6+9
			k0 = 4+9
			paths.append(1)
		else:
			x = 4+f6
			k0 = k0/7
			k0 = 8/1
			paths.append(2)
		if x > 4:
			k0 = 1-k0
			x = x+3
			f6 = f6*6
			paths.append(3)
		else:
			f6 = 3*3
			x = x/k0
			x = x/k0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))