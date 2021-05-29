import numpy as np 

def function(x):

	f1 = x
	k0 = 0
	x = 2
	paths = []
	try:
		if x >= 5:
			k0 = 6/k0
			f1 = f1-2
			paths.append(1)
		else:
			x = 6/6
			paths.append(2)
		if f1 >= 6:
			k0 = 2*0
			paths.append(3)
		else:
			x = 7+6
			k0 = k0+3
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		f1 = f1**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))