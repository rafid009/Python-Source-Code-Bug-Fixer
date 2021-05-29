import numpy as np 

def function(x):

	t6 = 4
	f7 = x
	paths = []
	try:
		if t6 <= 4:
			t6 = 3/t6
			paths.append(1)
		else:
			f7 = t6+f7
			f7 = t6*5
			x = x*t6
			paths.append(2)
		if t6 >= 2:
			f7 = 6-0
			paths.append(3)
		else:
			f7 = f7-6
			x = 5*x
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))