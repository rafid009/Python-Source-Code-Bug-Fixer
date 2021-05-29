import numpy as np 

def function(x):

	p4 = 4
	t6 = 0
	paths = []
	try:
		if x <= 2:
			p4 = p4-t6
			x = 7-2
			p4 = 9-2
			paths.append(1)
		else:
			p4 = p4-8
			paths.append(2)
		if x < 9:
			p4 = p4*p4
			x = x*t6
			paths.append(3)
		else:
			x = x+4
			t6 = 7-2
			t6 = p4*t6
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		x = t6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))