import numpy as np 

def function(x):

	t1 = x
	p7 = 0
	paths = []
	try:
		if x >= 1:
			p7 = p7*t1
			x = p7+x
			x = p7-p7
			paths.append(1)
		else:
			x = x*t1
			x = x-8
			paths.append(2)
		if p7 < 9:
			p7 = p7+0
			paths.append(3)
		else:
			t1 = 6-7
			x = 7*x
			t1 = t1-1
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		x = t1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))