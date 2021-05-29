import numpy as np 

def function(x):

	k4 = 1
	f9 = 4
	paths = []
	try:
		if k4 <= 9:
			f9 = x+5
			paths.append(1)
		else:
			k4 = k4/k4
			k4 = 6/k4
			x = 0*6
			paths.append(2)
		if k4 <= 5:
			f9 = 2-f9
			k4 = k4*x
			x = 8+8
			paths.append(3)
		else:
			k4 = k4+7
			f9 = f9+7
			f9 = f9+1
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))