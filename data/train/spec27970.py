import numpy as np 

def function(x):

	k1 = x
	f4 = 4
	paths = []
	try:
		if f4 <= 2:
			x = x+f4
			paths.append(1)
		else:
			k1 = x+6
			paths.append(2)
		if k1 >= 3:
			f4 = 0+x
			paths.append(3)
		else:
			x = x*9
			f4 = 8-x
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		f4 = f4**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))