import numpy as np 

def function(x):

	b5 = 6
	t9 = 0
	paths = []
	try:
		if b5 < 2:
			b5 = x-b5
			x = 8*x
			x = 0-6
			paths.append(1)
		else:
			x = 6*x
			t9 = x+b5
			paths.append(2)
		if t9 >= 3:
			b5 = x/6
			t9 = t9+2
			t9 = t9+2
			paths.append(3)
		else:
			x = b5/9
			t9 = 1-b5
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		t9 = t9**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))