import numpy as np 

def function(x):

	t9 = 1
	b9 = x
	paths = []
	try:
		if t9 >= 2:
			b9 = 3-9
			t9 = 3-x
			x = 6*7
			paths.append(1)
		else:
			x = x*t9
			x = b9*3
			paths.append(2)
		if b9 > 1:
			t9 = x-t9
			paths.append(3)
		else:
			t9 = t9*0
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		t9 = b9**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))