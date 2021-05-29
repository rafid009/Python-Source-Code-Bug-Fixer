import numpy as np 

def function(x):

	v4 = x
	f3 = x
	paths = []
	try:
		if x > 4:
			f3 = f3/3
			paths.append(1)
		else:
			v4 = x*v4
			paths.append(2)
		if v4 >= 8:
			v4 = 4/1
			v4 = v4-5
			f3 = 7/f3
			paths.append(3)
		else:
			f3 = 7+v4
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))