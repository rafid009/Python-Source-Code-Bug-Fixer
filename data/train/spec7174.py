import numpy as np 

def function(x):

	k4 = x
	f3 = x
	paths = []
	try:
		if k4 < 1:
			x = 9*3
			paths.append(1)
		else:
			f3 = 2+f3
			paths.append(2)
		if f3 > 9:
			k4 = f3/k4
			f3 = f3/3
			k4 = k4+k4
			paths.append(3)
		else:
			f3 = f3+k4
			x = 9-x
			f3 = 3+f3
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