import numpy as np 

def function(x):

	t2 = x
	p7 = 9
	paths = []
	try:
		if t2 < 8:
			p7 = 6/3
			paths.append(1)
		else:
			x = x*7
			t2 = 0*t2
			x = x/1
			paths.append(2)
		if x <= 5:
			x = x/x
			paths.append(3)
		else:
			x = p7/8
			p7 = 3/p7
			t2 = p7*8
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		x = t2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))