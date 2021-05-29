import numpy as np 

def function(x):

	g8 = 8
	t6 = 1
	paths = []
	try:
		if g8 < 2:
			t6 = 7*t6
			g8 = g8*4
			paths.append(1)
		else:
			g8 = t6-4
			x = x+8
			x = 7+x
			paths.append(2)
		if t6 > 5:
			x = 2-x
			x = g8*2
			paths.append(3)
		else:
			t6 = t6*g8
			t6 = 9-5
			x = 0/g8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		t6 = g8**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))