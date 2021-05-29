import numpy as np 

def function(x):

	t1 = x
	x6 = 6
	paths = []
	try:
		if x6 < 0:
			x = 0+x
			t1 = x*t1
			t1 = t1/t1
			paths.append(1)
		else:
			x = x/3
			x6 = t1*5
			paths.append(2)
		if x >= 7:
			x = x/5
			x6 = x6+x
			paths.append(3)
		else:
			x6 = x6/8
			x6 = 6-x6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x6 = x**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))