import numpy as np 

def function(x):

	t3 = 7
	k6 = x
	paths = []
	try:
		if x >= 9:
			t3 = t3*3
			paths.append(1)
		else:
			t3 = 9-t3
			paths.append(2)
		if x <= 7:
			t3 = t3+5
			t3 = 4*k6
			paths.append(3)
		else:
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		k6 = t3**0.5
		return k6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))