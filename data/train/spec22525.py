import numpy as np 

def function(x):

	g2 = x
	t1 = x
	paths = []
	try:
		if g2 > 8:
			t1 = t1+6
			paths.append(1)
		else:
			g2 = t1-6
			t1 = t1*9
			x = 7/x
			paths.append(2)
		if g2 >= 3:
			x = 0+g2
			x = x+4
			g2 = x+9
			paths.append(3)
		else:
			t1 = 6-t1
			x = x-6
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t1 = t1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))