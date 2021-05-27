import numpy as np 

def function(x):

	j9 = 8
	t8 = x
	paths = []
	try:
		if x <= 2:
			j9 = j9*x
			paths.append(1)
		else:
			j9 = 8-4
			t8 = 9-1
			j9 = j9+8
			paths.append(2)
		if x <= 1:
			t8 = 5*t8
			t8 = t8+2
			x = x+9
			paths.append(3)
		else:
			j9 = 3+j9
			j9 = j9-j9
			x = x/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))