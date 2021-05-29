import numpy as np 

def function(x):

	f8 = x
	k9 = 3
	paths = []
	try:
		if k9 >= 6:
			f8 = k9/f8
			k9 = 4+k9
			x = x+7
			paths.append(1)
		else:
			f8 = f8/6
			f8 = f8*6
			paths.append(2)
		if k9 < 4:
			f8 = 8/f8
			k9 = k9-8
			paths.append(3)
		else:
			f8 = 4/2
			x = x/k9
			f8 = k9*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))