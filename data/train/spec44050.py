import numpy as np 

def function(x):

	f8 = x
	v4 = x
	paths = []
	try:
		if v4 <= 9:
			v4 = x-4
			paths.append(1)
		else:
			v4 = v4*v4
			v4 = 0/3
			x = 5*x
			paths.append(2)
		if x > 1:
			v4 = v4*3
			paths.append(3)
		else:
			v4 = 1+v4
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		f8 = f8**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))