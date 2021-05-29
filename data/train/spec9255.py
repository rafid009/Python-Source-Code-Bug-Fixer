import numpy as np 

def function(x):

	j4 = 1
	t9 = 2
	x = x
	paths = []
	try:
		if t9 > 4:
			x = x+j4
			j4 = j4-x
			paths.append(1)
		else:
			t9 = 7-8
			j4 = x*j4
			x = x+2
			paths.append(2)
		if j4 < 3:
			t9 = t9/6
			t9 = j4/5
			paths.append(3)
		else:
			j4 = 8-1
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