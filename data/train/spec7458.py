import numpy as np 

def function(x):

	t3 = x
	x0 = x
	paths = []
	try:
		if t3 >= 2:
			x = x*t3
			t3 = x+t3
			paths.append(1)
		else:
			x0 = x0-x
			paths.append(2)
		if x0 > 7:
			t3 = x0/6
			x = 3*x
			paths.append(3)
		else:
			x = x*5
			x0 = 5-x0
			x = x+7
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x0 = t3**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))