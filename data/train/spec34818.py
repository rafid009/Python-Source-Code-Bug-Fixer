import numpy as np 

def function(x):

	k2 = 8
	f1 = x
	paths = []
	try:
		if x > 8:
			x = 6+f1
			k2 = k2+7
			k2 = k2/k2
			paths.append(1)
		else:
			k2 = x*k2
			k2 = 4*k2
			f1 = f1+0
			paths.append(2)
		if k2 < 2:
			x = x+7
			paths.append(3)
		else:
			f1 = f1/5
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		k2 = k2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))