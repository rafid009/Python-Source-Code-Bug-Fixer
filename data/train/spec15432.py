import numpy as np 

def function(x):

	t1 = 8
	x6 = 5
	x = x
	paths = []
	try:
		if t1 <= 1:
			x = x+x6
			x6 = 5+7
			t1 = t1-x
			paths.append(1)
		else:
			x = 4*x
			x6 = 8*3
			x = x+x6
			paths.append(2)
		if x < 0:
			x = x6+x
			paths.append(3)
		else:
			t1 = x-x6
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		x6 = t1**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))