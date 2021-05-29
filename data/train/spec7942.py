import numpy as np 

def function(x):

	v7 = x
	t1 = 5
	paths = []
	try:
		if t1 > 4:
			v7 = v7-2
			x = x/v7
			x = x*v7
			paths.append(1)
		else:
			v7 = v7+7
			x = x-7
			x = x*2
			paths.append(2)
		if x < 4:
			v7 = v7+v7
			t1 = t1*4
			paths.append(3)
		else:
			v7 = 7*v7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))