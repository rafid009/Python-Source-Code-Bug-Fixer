import numpy as np 

def function(x):

	r3 = 1
	t9 = x
	paths = []
	try:
		if t9 <= 3:
			x = 8*x
			paths.append(1)
		else:
			r3 = 9-r3
			x = x+2
			paths.append(2)
		if t9 <= 3:
			t9 = t9+9
			x = t9/r3
			r3 = r3+4
			paths.append(3)
		else:
			t9 = x*r3
			r3 = r3-9
			t9 = t9/7
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