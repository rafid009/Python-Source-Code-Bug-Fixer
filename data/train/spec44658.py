import numpy as np 

def function(x):

	p6 = x
	t6 = x
	paths = []
	try:
		if x < 6:
			p6 = p6-8
			t6 = 8+p6
			t6 = t6/t6
			paths.append(1)
		else:
			p6 = 2/p6
			p6 = 6-p6
			paths.append(2)
		if p6 >= 0:
			t6 = 0/6
			t6 = x-8
			paths.append(3)
		else:
			t6 = 0/9
			t6 = 1*x
			x = x*6
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