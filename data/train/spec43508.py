import numpy as np 

def function(x):

	t3 = x
	a8 = 0
	x = x
	paths = []
	try:
		if x >= 4:
			t3 = 0+1
			paths.append(1)
		else:
			a8 = a8-4
			paths.append(2)
		if t3 < 0:
			t3 = 6+t3
			paths.append(3)
		else:
			t3 = t3-3
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		x = t3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))