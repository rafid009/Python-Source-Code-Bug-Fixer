import numpy as np 

def function(x):

	t5 = 1
	g2 = 2
	paths = []
	try:
		if g2 >= 3:
			x = g2-x
			t5 = t5+4
			paths.append(1)
		else:
			t5 = t5+0
			g2 = 5-t5
			paths.append(2)
		if t5 < 7:
			t5 = t5*7
			paths.append(3)
		else:
			g2 = 2*g2
			t5 = t5+g2
			x = 8+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t5 = x**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))