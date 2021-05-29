import numpy as np 

def function(x):

	t8 = x
	p4 = x
	paths = []
	try:
		if t8 <= 5:
			x = 2/5
			paths.append(1)
		else:
			p4 = p4+p4
			paths.append(2)
		if t8 < 4:
			p4 = p4*2
			x = 9*x
			t8 = 4*t8
			paths.append(3)
		else:
			t8 = t8+4
			t8 = t8-2
			p4 = 2-6
			paths.append(4)
		paths.append(5)
		assert p4 >= 0
		p4 = p4**0.5
		return p4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))