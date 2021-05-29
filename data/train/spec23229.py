import numpy as np 

def function(x):

	p3 = 7
	t6 = 7
	paths = []
	try:
		if x <= 7:
			p3 = 0/1
			x = x*2
			paths.append(1)
		else:
			x = t6-6
			p3 = p3/t6
			paths.append(2)
		if x >= 9:
			t6 = t6-x
			p3 = p3-2
			t6 = p3+t6
			paths.append(3)
		else:
			x = x-p3
			t6 = x/2
			p3 = p3*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))