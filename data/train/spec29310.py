import numpy as np 

def function(x):

	p1 = x
	t6 = 8
	paths = []
	try:
		if t6 < 1:
			t6 = t6/9
			p1 = x+p1
			p1 = p1-6
			paths.append(1)
		else:
			p1 = p1+t6
			paths.append(2)
		if p1 > 2:
			t6 = t6/2
			t6 = t6/t6
			t6 = 4/3
			paths.append(3)
		else:
			t6 = 1+t6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p1 = x**0.5
		return p1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))