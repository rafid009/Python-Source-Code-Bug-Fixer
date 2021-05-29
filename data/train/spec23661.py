import numpy as np 

def function(x):

	p6 = x
	t3 = x
	paths = []
	try:
		if x >= 5:
			p6 = t3/5
			t3 = x*8
			paths.append(1)
		else:
			p6 = 8-8
			x = 3-x
			paths.append(2)
		if t3 <= 7:
			p6 = 7+p6
			paths.append(3)
		else:
			t3 = x+8
			t3 = 2+p6
			t3 = t3/p6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))