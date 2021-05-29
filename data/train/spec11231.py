import numpy as np 

def function(x):

	t5 = 8
	x2 = x
	paths = []
	try:
		if x > 9:
			x = x/t5
			t5 = 8-t5
			x = t5+x
			paths.append(1)
		else:
			x = x2/3
			x2 = 6-6
			paths.append(2)
		if t5 >= 0:
			t5 = t5*t5
			paths.append(3)
		else:
			x = 4-t5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))