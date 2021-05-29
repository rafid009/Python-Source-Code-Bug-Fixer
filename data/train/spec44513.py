import numpy as np 

def function(x):

	t7 = x
	x5 = x
	paths = []
	try:
		if x5 <= 0:
			t7 = x+t7
			t7 = 4/t7
			x5 = x*x5
			paths.append(1)
		else:
			x5 = x5-x5
			paths.append(2)
		if t7 < 6:
			x5 = x5*5
			x = x5*7
			x = x+x5
			paths.append(3)
		else:
			x5 = 1-9
			x5 = x5*9
			t7 = 0+7
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x5 = t7**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))