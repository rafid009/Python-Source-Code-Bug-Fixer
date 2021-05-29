import numpy as np 

def function(x):

	p4 = x
	t6 = 0
	paths = []
	try:
		if x > 9:
			x = 6-x
			p4 = 8-1
			p4 = p4*8
			paths.append(1)
		else:
			t6 = 3-1
			p4 = p4-5
			paths.append(2)
		if x > 6:
			p4 = x/p4
			paths.append(3)
		else:
			t6 = 2*1
			t6 = t6/t6
			p4 = p4+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t6 = x**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))