import numpy as np 

def function(x):

	t6 = x
	u6 = 2
	paths = []
	try:
		if u6 < 4:
			x = 0+x
			paths.append(1)
		else:
			u6 = 1+u6
			paths.append(2)
		if u6 < 2:
			t6 = 1-u6
			t6 = t6*9
			x = t6+7
			paths.append(3)
		else:
			x = t6/x
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))