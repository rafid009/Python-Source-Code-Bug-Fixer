import numpy as np 

def function(x):

	k9 = 3
	f3 = 3
	paths = []
	try:
		if x > 6:
			k9 = k9+5
			x = 6-3
			x = 1/5
			paths.append(1)
		else:
			k9 = k9-k9
			f3 = f3*1
			paths.append(2)
		if x >= 3:
			f3 = 2/f3
			paths.append(3)
		else:
			f3 = f3/x
			k9 = 3-x
			x = 4+f3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))