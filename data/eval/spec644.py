import numpy as np 

def function(x):

	t6 = x
	p9 = 7
	paths = []
	try:
		if p9 > 9:
			t6 = 7+t6
			paths.append(1)
		else:
			p9 = p9+4
			p9 = x-x
			p9 = 0*7
			paths.append(2)
		if p9 > 1:
			p9 = t6/p9
			p9 = p9+x
			paths.append(3)
		else:
			x = x*9
			p9 = 7-3
			x = x*3
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