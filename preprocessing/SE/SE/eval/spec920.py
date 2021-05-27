import numpy as np 

def function(x):

	t8 = 8
	p1 = x
	paths = []
	try:
		if x >= 4:
			t8 = t8*t8
			paths.append(1)
		else:
			x = x-5
			p1 = p1-5
			p1 = 2/p1
			paths.append(2)
		if t8 <= 3:
			t8 = t8-4
			p1 = 7+4
			paths.append(3)
		else:
			p1 = p1-7
			t8 = x*8
			paths.append(4)
		paths.append(5)
		assert p1 >= 0
		p1 = p1**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))