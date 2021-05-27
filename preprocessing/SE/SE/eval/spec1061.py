import numpy as np 

def function(x):

	g9 = 9
	t7 = x
	paths = []
	try:
		if x > 2:
			x = g9-x
			g9 = t7*8
			g9 = g9/8
			paths.append(1)
		else:
			x = x+g9
			x = x*3
			paths.append(2)
		if g9 <= 3:
			x = x*6
			t7 = x*1
			x = x*2
			paths.append(3)
		else:
			g9 = g9-x
			x = x-2
			t7 = 8-t7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t7 = x**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))