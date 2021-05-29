import numpy as np 

def function(x):

	p6 = x
	t8 = x
	paths = []
	try:
		if t8 > 4:
			x = 1*1
			paths.append(1)
		else:
			t8 = p6/t8
			x = x+4
			p6 = p6/4
			paths.append(2)
		if t8 <= 1:
			t8 = 9/1
			x = 5-x
			t8 = t8-5
			paths.append(3)
		else:
			t8 = 3*t8
			x = 5/x
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