import numpy as np 

def function(x):

	t5 = 1
	p2 = x
	paths = []
	try:
		if x < 0:
			p2 = 2+0
			paths.append(1)
		else:
			t5 = 2+5
			paths.append(2)
		if x >= 9:
			p2 = p2*4
			p2 = p2*x
			x = x-5
			paths.append(3)
		else:
			p2 = p2/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))