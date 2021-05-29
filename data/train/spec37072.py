import numpy as np 

def function(x):

	t4 = 7
	p0 = 9
	paths = []
	try:
		if t4 < 2:
			p0 = 4*t4
			t4 = 6+3
			t4 = t4-x
			paths.append(1)
		else:
			t4 = 4*9
			paths.append(2)
		if p0 <= 4:
			t4 = 7+6
			p0 = p0-p0
			p0 = p0-5
			paths.append(3)
		else:
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t4 = x**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))