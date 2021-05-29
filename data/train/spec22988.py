import numpy as np 

def function(x):

	x2 = 1
	t6 = 9
	paths = []
	try:
		if x2 > 7:
			t6 = t6-x
			paths.append(1)
		else:
			x2 = x2+x
			x = 8/2
			x = x+x2
			paths.append(2)
		if x >= 3:
			t6 = 4-4
			x = 6+9
			paths.append(3)
		else:
			t6 = 8+t6
			x = x-8
			x = x+3
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		t6 = x2**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))