import numpy as np 

def function(x):

	u7 = 2
	t2 = 8
	paths = []
	try:
		if u7 <= 3:
			x = 6+x
			t2 = u7*3
			t2 = 7/8
			paths.append(1)
		else:
			x = x-x
			u7 = u7-5
			paths.append(2)
		if x >= 6:
			u7 = u7-u7
			u7 = 1/t2
			paths.append(3)
		else:
			x = 0-x
			t2 = t2*0
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