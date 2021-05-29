import numpy as np 

def function(x):

	k3 = 9
	f4 = x
	paths = []
	try:
		if f4 <= 8:
			x = x*x
			paths.append(1)
		else:
			k3 = k3/f4
			x = 7-x
			paths.append(2)
		if x <= 2:
			x = x*6
			f4 = 2/f4
			paths.append(3)
		else:
			f4 = 8/f4
			x = 2+x
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