import numpy as np 

def function(x):

	r0 = 7
	t9 = 1
	paths = []
	try:
		if r0 <= 3:
			x = 8*x
			t9 = 4*9
			t9 = x-t9
			paths.append(1)
		else:
			r0 = 4+r0
			r0 = 9-5
			paths.append(2)
		if x < 5:
			r0 = 4+3
			paths.append(3)
		else:
			r0 = t9-6
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		t9 = r0**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))