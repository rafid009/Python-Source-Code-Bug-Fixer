import numpy as np 

def function(x):

	t9 = x
	r9 = 7
	paths = []
	try:
		if x > 7:
			t9 = t9-5
			x = x+9
			paths.append(1)
		else:
			r9 = 9/t9
			paths.append(2)
		if r9 < 8:
			x = 0+x
			r9 = 4+r9
			x = x*1
			paths.append(3)
		else:
			x = x-t9
			t9 = t9/1
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