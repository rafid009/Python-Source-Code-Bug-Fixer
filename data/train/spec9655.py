import numpy as np 

def function(x):

	t2 = x
	paths = []
	try:
		if t2 < 9:
			x = 4+x
			paths.append(1)
		else:
			t2 = t2/8
			paths.append(2)
		if t2 > 1:
			x = 7*t2
			x = x-8
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		t2 = t2**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))