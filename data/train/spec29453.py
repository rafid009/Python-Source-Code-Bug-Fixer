import numpy as np 

def function(x):

	t7 = x
	k4 = x
	paths = []
	try:
		if k4 >= 0:
			t7 = 6*0
			paths.append(1)
		else:
			x = t7/k4
			paths.append(2)
		if x <= 8:
			x = 9/x
			k4 = k4+8
			paths.append(3)
		else:
			k4 = k4-k4
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		t7 = t7**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))