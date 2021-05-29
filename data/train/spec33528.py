import numpy as np 

def function(x):

	b2 = x
	t6 = 1
	paths = []
	try:
		if b2 > 9:
			t6 = 4+t6
			t6 = 9*t6
			paths.append(1)
		else:
			t6 = x*3
			b2 = t6/3
			t6 = 8/t6
			paths.append(2)
		if x > 9:
			t6 = 4*4
			paths.append(3)
		else:
			t6 = t6-9
			x = x+9
			t6 = t6+t6
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		t6 = b2**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))