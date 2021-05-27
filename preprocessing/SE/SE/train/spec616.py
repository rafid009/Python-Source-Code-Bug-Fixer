import numpy as np 

def function(x):

	t9 = 8
	p3 = 6
	paths = []
	try:
		if t9 >= 6:
			p3 = t9*p3
			p3 = p3*9
			t9 = 9/t9
			paths.append(1)
		else:
			t9 = 4*t9
			t9 = 6-2
			t9 = t9/9
			paths.append(2)
		if x > 5:
			p3 = 8*p3
			p3 = p3-2
			x = 8+x
			paths.append(3)
		else:
			p3 = p3-t9
			t9 = 9*8
			p3 = p3/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))