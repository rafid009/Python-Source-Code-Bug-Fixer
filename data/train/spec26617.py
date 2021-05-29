import numpy as np 

def function(x):

	i0 = 3
	t9 = x
	paths = []
	try:
		if t9 <= 0:
			x = 8-x
			paths.append(1)
		else:
			x = 9+x
			i0 = i0-3
			t9 = 5/5
			paths.append(2)
		if x > 5:
			i0 = i0-3
			i0 = i0-8
			paths.append(3)
		else:
			t9 = 3/1
			i0 = x-i0
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