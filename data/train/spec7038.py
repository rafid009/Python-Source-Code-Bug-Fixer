import numpy as np 

def function(x):

	p2 = 2
	t6 = x
	paths = []
	try:
		if x >= 5:
			x = x*p2
			paths.append(1)
		else:
			p2 = p2+x
			paths.append(2)
		if p2 < 8:
			t6 = p2+3
			x = 7*7
			paths.append(3)
		else:
			t6 = 8*t6
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))