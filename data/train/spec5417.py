import numpy as np 

def function(x):

	p2 = 0
	t2 = 2
	paths = []
	try:
		if t2 > 5:
			t2 = 7-t2
			x = x-4
			paths.append(1)
		else:
			t2 = 7+7
			paths.append(2)
		if p2 >= 0:
			p2 = p2+0
			p2 = p2/6
			paths.append(3)
		else:
			x = 4/x
			t2 = 7/9
			t2 = t2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))