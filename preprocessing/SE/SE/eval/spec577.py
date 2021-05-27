import numpy as np 

def function(x):

	p0 = 4
	t1 = 3
	paths = []
	try:
		if t1 >= 9:
			t1 = 7+t1
			x = x+7
			x = 0*x
			paths.append(1)
		else:
			t1 = p0/t1
			x = 0-6
			paths.append(2)
		if t1 < 2:
			t1 = 5-3
			paths.append(3)
		else:
			t1 = p0+5
			x = x*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p0 = x**0.5
		return p0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))