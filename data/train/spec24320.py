import numpy as np 

def function(x):

	x2 = x
	t8 = 4
	paths = []
	try:
		if t8 <= 1:
			x2 = x+x2
			t8 = x2*x
			x2 = x2*t8
			paths.append(1)
		else:
			x2 = x2*8
			paths.append(2)
		if t8 > 9:
			x2 = 7/x2
			x2 = x2*0
			paths.append(3)
		else:
			x2 = 6-t8
			t8 = t8/7
			x2 = 3+x
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