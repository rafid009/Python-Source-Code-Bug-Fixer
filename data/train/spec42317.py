import numpy as np 

def function(x):

	p2 = 2
	t7 = x
	paths = []
	try:
		if x >= 1:
			x = 8+t7
			p2 = p2-5
			x = x*6
			paths.append(1)
		else:
			p2 = p2+3
			x = 6+x
			p2 = 8*x
			paths.append(2)
		if x > 2:
			t7 = 3-t7
			t7 = x*7
			paths.append(3)
		else:
			t7 = t7/p2
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		t7 = p2**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))