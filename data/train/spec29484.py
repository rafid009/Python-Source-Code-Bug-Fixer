import numpy as np 

def function(x):

	t1 = 9
	b8 = x
	paths = []
	try:
		if t1 > 9:
			t1 = t1*8
			b8 = 1-5
			t1 = t1+6
			paths.append(1)
		else:
			b8 = b8+x
			paths.append(2)
		if t1 <= 8:
			b8 = b8+t1
			paths.append(3)
		else:
			x = x*3
			t1 = t1*b8
			t1 = 0-t1
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		t1 = b8**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))