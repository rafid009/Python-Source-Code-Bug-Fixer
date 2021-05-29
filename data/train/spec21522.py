import numpy as np 

def function(x):

	i6 = 2
	f4 = x
	paths = []
	try:
		if x < 1:
			x = x-x
			paths.append(1)
		else:
			i6 = i6*5
			i6 = 3*0
			paths.append(2)
		if x >= 3:
			x = 1*x
			x = 7/f4
			x = 9-8
			paths.append(3)
		else:
			x = i6*x
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