import numpy as np 

def function(x):

	r2 = x
	t9 = 4
	paths = []
	try:
		if x <= 6:
			r2 = r2/4
			r2 = 8/r2
			x = x/2
			paths.append(1)
		else:
			x = 5*x
			t9 = t9-t9
			x = x*3
			paths.append(2)
		if x < 7:
			x = 8/x
			paths.append(3)
		else:
			x = x+x
			t9 = 8+r2
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		t9 = r2**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))