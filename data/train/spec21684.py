import numpy as np 

def function(x):

	p9 = 6
	t9 = 1
	paths = []
	try:
		if p9 <= 9:
			x = x+p9
			t9 = 9*t9
			paths.append(1)
		else:
			p9 = x/p9
			paths.append(2)
		if t9 >= 4:
			p9 = 4/x
			paths.append(3)
		else:
			x = 0/x
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