import numpy as np 

def function(x):

	v6 = x
	f7 = x
	paths = []
	try:
		if x >= 5:
			v6 = x*x
			paths.append(1)
		else:
			v6 = v6+7
			paths.append(2)
		if x >= 2:
			f7 = f7+7
			x = 8+2
			paths.append(3)
		else:
			f7 = f7-v6
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		f7 = f7**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))