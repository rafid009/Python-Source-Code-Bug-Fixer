import numpy as np 

def function(x):

	j2 = 8
	t9 = x
	x = 5
	paths = []
	try:
		if x <= 3:
			x = x/t9
			paths.append(1)
		else:
			t9 = 8/j2
			x = 2+j2
			x = 3-x
			paths.append(2)
		if j2 <= 4:
			t9 = j2/t9
			j2 = 3+j2
			paths.append(3)
		else:
			x = x-6
			t9 = t9-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))