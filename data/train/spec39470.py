import numpy as np 

def function(x):

	p3 = 7
	t9 = 4
	paths = []
	try:
		if t9 > 1:
			p3 = p3*0
			p3 = p3+6
			paths.append(1)
		else:
			t9 = t9-1
			paths.append(2)
		if x >= 0:
			x = x-t9
			x = x*2
			t9 = t9-8
			paths.append(3)
		else:
			x = x-x
			p3 = 1/p3
			x = p3/2
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