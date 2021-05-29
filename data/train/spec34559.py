import numpy as np 

def function(x):

	t4 = 2
	f3 = x
	paths = []
	try:
		if t4 >= 1:
			x = x-5
			x = x*f3
			t4 = t4-x
			paths.append(1)
		else:
			t4 = t4*9
			paths.append(2)
		if x >= 8:
			f3 = 7+1
			f3 = f3+8
			paths.append(3)
		else:
			x = 5+x
			x = x-5
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