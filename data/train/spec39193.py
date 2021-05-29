import numpy as np 

def function(x):

	p9 = 9
	t9 = 7
	paths = []
	try:
		if x > 6:
			p9 = 6+p9
			paths.append(1)
		else:
			x = 7+x
			paths.append(2)
		if p9 >= 9:
			t9 = 0*2
			x = x*3
			p9 = 9/p9
			paths.append(3)
		else:
			t9 = t9+t9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))