import numpy as np 

def function(x):

	t8 = 0
	p9 = x
	paths = []
	try:
		if x > 1:
			p9 = t8+8
			x = 0+p9
			paths.append(1)
		else:
			x = x*p9
			x = 4+p9
			paths.append(2)
		if x > 9:
			x = 4*x
			t8 = p9*t8
			x = 1-x
			paths.append(3)
		else:
			p9 = p9-5
			x = 5-2
			t8 = 7*2
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		t8 = p9**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))