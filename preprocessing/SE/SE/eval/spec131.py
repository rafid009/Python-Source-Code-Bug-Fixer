import numpy as np 

def function(x):

	v1 = x
	f4 = 1
	paths = []
	try:
		if f4 <= 8:
			f4 = f4-9
			f4 = v1+1
			paths.append(1)
		else:
			f4 = f4-0
			v1 = v1/6
			x = 5-0
			paths.append(2)
		if f4 > 1:
			v1 = 7-2
			paths.append(3)
		else:
			v1 = v1*v1
			x = v1*x
			v1 = v1-7
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))