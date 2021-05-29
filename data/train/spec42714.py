import numpy as np 

def function(x):

	t9 = 5
	l8 = x
	paths = []
	try:
		if t9 > 1:
			x = x+x
			x = x*1
			t9 = x*2
			paths.append(1)
		else:
			t9 = t9+t9
			l8 = l8+3
			paths.append(2)
		if x >= 3:
			t9 = t9-2
			l8 = l8*4
			paths.append(3)
		else:
			t9 = t9-7
			t9 = t9/6
			l8 = 2-t9
			paths.append(4)
		paths.append(5)
		assert t9 >= 0
		l8 = t9**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))