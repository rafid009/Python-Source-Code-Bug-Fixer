import numpy as np 

def function(x):

	t6 = x
	a5 = 6
	paths = []
	try:
		if x < 8:
			t6 = 6+3
			paths.append(1)
		else:
			x = 1/5
			paths.append(2)
		if a5 < 6:
			t6 = t6*5
			paths.append(3)
		else:
			a5 = 6*6
			t6 = t6+x
			a5 = a5-7
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))