import numpy as np 

def function(x):

	p3 = 9
	t9 = 6
	paths = []
	try:
		if x < 6:
			p3 = p3/t9
			paths.append(1)
		else:
			t9 = 5/t9
			t9 = t9*t9
			paths.append(2)
		if x < 8:
			t9 = 6-6
			x = x-0
			x = x+x
			paths.append(3)
		else:
			x = x-6
			p3 = x/4
			p3 = t9-p3
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))